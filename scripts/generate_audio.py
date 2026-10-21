"""Convierte a MP3 cada episodio de episodes/*.md que todavía no tenga release.

Cada episodio se publica como un GitHub Release con tag ep-<nombre-del-archivo>
y el MP3 adjunto. Usa Google Cloud TTS si hay GOOGLE_TTS_API_KEY y, si falla, edge-tts.
"""

import asyncio
import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EPISODES_DIR = ROOT / "episodes"

EDGE_VOICE = os.environ.get("EDGE_VOICE", "es-AR-TomasNeural")
EDGE_RATE = os.environ.get("EDGE_RATE", "+0%")
GOOGLE_KEY = os.environ.get("GOOGLE_TTS_API_KEY", "").strip()
GOOGLE_VOICE = os.environ.get("GOOGLE_VOICE", "es-US-Chirp3-HD-Charon")


def parse_episode(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    meta, body = {}, raw
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if match:
        for line in match.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip().strip('"')
        body = match.group(2)
    meta["slug"] = path.stem
    meta["tag"] = f"ep-{path.stem}"
    meta["body"] = body
    return meta


def to_speech_text(markdown: str) -> str:
    """Quita la sintaxis markdown y deja pausas entre secciones."""
    lines = []
    for line in markdown.splitlines():
        line = line.strip()
        if not line:
            lines.append("")
            continue
        line = re.sub(r"^#+\s*", "", line)
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"\*\*|__|\*|_|`", "", line)
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        if not re.search(r"[.!?:…]$", line):
            line += "."
        lines.append(line)
    text = "\n".join(lines)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def release_exists(tag: str) -> bool:
    result = subprocess.run(
        ["gh", "release", "view", tag], capture_output=True, text=True
    )
    return result.returncode == 0


async def edge_synthesize(text: str, out: Path) -> None:
    import edge_tts

    communicate = edge_tts.Communicate(text, EDGE_VOICE, rate=EDGE_RATE)
    await communicate.save(str(out))


def split_sections(markdown: str) -> list[str]:
    """Separa el guion en secciones usando los encabezados markdown."""
    sections, current = [], []
    for line in markdown.splitlines():
        if line.lstrip().startswith("#") and current:
            sections.append("\n".join(current))
            current = []
        current.append(line)
    if current:
        sections.append("\n".join(current))
    return [t for t in (to_speech_text(sec) for sec in sections) if t]


def chunk_text(text: str, limit: int = 4500) -> list[str]:
    """La API acepta hasta 5000 bytes por pedido: se parte por párrafos."""
    chunks, current = [], ""
    for paragraph in text.split("\n\n"):
        candidate = f"{current}\n\n{paragraph}".strip()
        if len(candidate.encode("utf-8")) > limit and current:
            chunks.append(current)
            current = paragraph
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


def google_request(text: str, out: Path) -> None:
    language = "-".join(GOOGLE_VOICE.split("-")[:2])
    payload = json.dumps({
        "input": {"text": text},
        "voice": {"languageCode": language, "name": GOOGLE_VOICE},
        "audioConfig": {"audioEncoding": "LINEAR16", "sampleRateHertz": 24000},
    }).encode("utf-8")
    request = urllib.request.Request(
        f"https://texttospeech.googleapis.com/v1/text:synthesize?key={GOOGLE_KEY}",
        data=payload, headers={"Content-Type": "application/json"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                out.write_bytes(base64.b64decode(json.load(response)["audioContent"]))
            return
        except urllib.error.HTTPError as error:
            detail = error.read().decode()[:400]
            if error.code < 500 and error.code != 429 or attempt == 2:
                raise RuntimeError(f"Google TTS HTTP {error.code}: {detail}") from error
        except urllib.error.URLError:
            if attempt == 2:
                raise
        time.sleep(5 * (attempt + 1))


def google_synthesize(markdown: str, out: Path) -> None:
    """Sintetiza por secciones y las une con silencios para marcar el cambio de tema."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        silence = {}
        for name, seconds in (("pausa_corta", 0.35), ("pausa_larga", 1.2)):
            silence[name] = tmp_path / f"{name}.wav"
            subprocess.run(
                ["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi",
                 "-i", "anullsrc=r=24000:cl=mono", "-t", str(seconds),
                 "-c:a", "pcm_s16le", str(silence[name])],
                check=True,
            )
        parts = []
        for s_index, section in enumerate(split_sections(markdown)):
            if s_index:
                parts.append(silence["pausa_larga"])
            for c_index, chunk in enumerate(chunk_text(section)):
                if c_index:
                    parts.append(silence["pausa_corta"])
                part = tmp_path / f"{s_index:03d}_{c_index:02d}.wav"
                google_request(chunk, part)
                parts.append(part)
        listing = tmp_path / "list.txt"
        listing.write_text("".join(f"file '{p}'\n" for p in parts))
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
             "-i", str(listing), "-ac", "1", "-codec:a", "libmp3lame", "-b:a", "64k",
             str(out)],
            check=True,
        )


def synthesize(markdown: str, out: Path) -> str:
    """Usa Google si hay API key; si falla (o no hay key), cae a edge-tts."""
    if GOOGLE_KEY:
        try:
            google_synthesize(markdown, out)
            return f"Google Cloud TTS ({GOOGLE_VOICE})"
        except Exception as error:  # noqa: BLE001
            print(f"::warning::Google TTS falló, uso edge-tts: {error}")
    asyncio.run(edge_synthesize(to_speech_text(markdown), out))
    if not out.exists() or out.stat().st_size < 10_000:
        raise RuntimeError("edge-tts devolvió un archivo vacío")
    return f"edge-tts ({EDGE_VOICE})"


def duration_seconds(path: Path) -> int:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True, check=True,
    )
    return round(float(result.stdout.strip()))


def main() -> None:
    from generate_cover import make_cover

    pending = [
        parse_episode(p)
        for p in sorted(EPISODES_DIR.glob("*.md"))
        if not release_exists(f"ep-{p.stem}")
    ]
    if not pending:
        print("No hay episodios nuevos.")
        return

    out_dir = ROOT / "build"
    out_dir.mkdir(exist_ok=True)
    for episode in pending:
        mp3 = out_dir / f"{episode['slug']}.mp3"
        engine = synthesize(episode["body"], mp3)
        seconds = duration_seconds(mp3)
        # La portada nunca debe frenar la publicación del episodio.
        cover = out_dir / f"{episode['slug']}.jpg"
        try:
            cover_method = make_cover(episode, cover)
            cover_files = [str(cover)]
        except Exception as error:  # noqa: BLE001
            print(f"::warning::No se pudo generar la portada: {error}")
            cover_method, cover_files = "sin portada", []
        notes = json.dumps({
            "description": episode.get("description", ""),
            "topic": episode.get("topic", ""),
            "date": episode.get("date", ""),
            "duration": seconds,
            "engine": engine,
            "cover": cover_method,
        }, ensure_ascii=False)
        subprocess.run(
            ["gh", "release", "create", episode["tag"], str(mp3), *cover_files,
             "--title", episode.get("title", episode["slug"]),
             "--notes", notes, "--latest"],
            check=True,
        )
        print(f"Publicado {episode['tag']}: {seconds // 60} min, {engine}, portada: {cover_method}")


if __name__ == "__main__":
    main()
