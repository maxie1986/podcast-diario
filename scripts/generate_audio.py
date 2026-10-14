"""Convierte a MP3 cada episodio de episodes/*.md que todavía no tenga release.

Cada episodio se publica como un GitHub Release con tag ep-<nombre-del-archivo>
y el MP3 adjunto. Usa edge-tts y, si falla y hay GOOGLE_TTS_API_KEY, Google Cloud TTS.
"""

import asyncio
import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EPISODES_DIR = ROOT / "episodes"

EDGE_VOICE = os.environ.get("EDGE_VOICE", "es-AR-TomasNeural")
EDGE_RATE = os.environ.get("EDGE_RATE", "+0%")
GOOGLE_KEY = os.environ.get("GOOGLE_TTS_API_KEY", "").strip()
GOOGLE_VOICE = os.environ.get("GOOGLE_VOICE", "es-US-Neural2-B")


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


def google_synthesize(text: str, out: Path) -> None:
    # La API acepta hasta 5000 bytes por pedido: se parte por párrafos.
    chunks, current = [], ""
    for paragraph in text.split("\n\n"):
        candidate = f"{current}\n\n{paragraph}".strip()
        if len(candidate.encode("utf-8")) > 4500 and current:
            chunks.append(current)
            current = paragraph
        else:
            current = candidate
    if current:
        chunks.append(current)

    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={GOOGLE_KEY}"
    language = "-".join(GOOGLE_VOICE.split("-")[:2])
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for i, chunk in enumerate(chunks):
            payload = json.dumps({
                "input": {"text": chunk},
                "voice": {"languageCode": language, "name": GOOGLE_VOICE},
                "audioConfig": {"audioEncoding": "MP3", "sampleRateHertz": 24000},
            }).encode("utf-8")
            request = urllib.request.Request(
                url, data=payload, headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(request, timeout=120) as response:
                audio = base64.b64decode(json.load(response)["audioContent"])
            part = Path(tmp) / f"{i:03d}.mp3"
            part.write_bytes(audio)
            parts.append(part)
        listing = Path(tmp) / "list.txt"
        listing.write_text("".join(f"file '{p}'\n" for p in parts))
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
             "-i", str(listing), "-c", "copy", str(out)],
            check=True,
        )


def synthesize(text: str, out: Path) -> str:
    try:
        asyncio.run(edge_synthesize(text, out))
        if out.exists() and out.stat().st_size > 10_000:
            return f"edge-tts ({EDGE_VOICE})"
        raise RuntimeError("edge-tts devolvió un archivo vacío")
    except Exception as error:  # noqa: BLE001
        print(f"edge-tts falló: {error}", file=sys.stderr)
        if not GOOGLE_KEY:
            raise
    google_synthesize(text, out)
    return f"Google Cloud TTS ({GOOGLE_VOICE})"


def duration_seconds(path: Path) -> int:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True, check=True,
    )
    return round(float(result.stdout.strip()))


def main() -> None:
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
        text = to_speech_text(episode["body"])
        mp3 = out_dir / f"{episode['slug']}.mp3"
        engine = synthesize(text, mp3)
        seconds = duration_seconds(mp3)
        notes = json.dumps({
            "description": episode.get("description", ""),
            "topic": episode.get("topic", ""),
            "date": episode.get("date", ""),
            "duration": seconds,
            "engine": engine,
        }, ensure_ascii=False)
        subprocess.run(
            ["gh", "release", "create", episode["tag"], str(mp3),
             "--title", episode.get("title", episode["slug"]),
             "--notes", notes, "--latest"],
            check=True,
        )
        print(f"Publicado {episode['tag']}: {seconds // 60} min, {engine}")


if __name__ == "__main__":
    main()
