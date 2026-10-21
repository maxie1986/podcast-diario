"""Genera muestras cortas con varias voces de Google Cloud TTS para compararlas.

Toma el arranque del primer episodio, lo sintetiza con cada voz de VOICES y
sube los MP3 al release "muestras-voces" (no afecta al feed).
"""

import base64
import json
import os
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_audio  # noqa: E402
from generate_audio import parse_episode, to_speech_text  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
KEY = os.environ.get("GOOGLE_TTS_API_KEY", "").strip()
VOICES = [v.strip() for v in os.environ.get("VOICES", "").split(",") if v.strip()]
TAG = "muestras-voces"
SAMPLE_CHARS = 1400  # unos 80 segundos de audio


def sample_text() -> str:
    episode = parse_episode(sorted((ROOT / "episodes").glob("*.md"))[0])
    text = to_speech_text(episode["body"])
    cut = text[:SAMPLE_CHARS]
    return cut[: cut.rfind(".") + 1]


def synthesize(text: str, voice: str, out: Path) -> None:
    language = "-".join(voice.split("-")[:2])
    payload = json.dumps({
        "input": {"text": text},
        "voice": {"languageCode": language, "name": voice},
        "audioConfig": {"audioEncoding": "LINEAR16"},
    }).encode("utf-8")
    request = urllib.request.Request(
        f"https://texttospeech.googleapis.com/v1/text:synthesize?key={KEY}",
        data=payload, headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            audio = base64.b64decode(json.load(response)["audioContent"])
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"{voice}: HTTP {error.code} {error.read().decode()[:600]}")
    with tempfile.NamedTemporaryFile(suffix=".wav") as wav:
        wav.write(audio)
        wav.flush()
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", wav.name,
             "-codec:a", "libmp3lame", "-b:a", "96k", str(out)],
            check=True,
        )


def main() -> None:
    if not KEY:
        print("::error::Falta el secret GOOGLE_TTS_API_KEY (o está vacío)")
        sys.exit(1)
    out_dir = ROOT / "build" / "muestras"
    out_dir.mkdir(parents=True, exist_ok=True)
    files, errors = [], []
    episode_slug = os.environ.get("EPISODE", "").strip()
    if episode_slug:
        # Prueba de punta a punta con el mismo código que usa el podcast.
        episode = parse_episode(ROOT / "episodes" / f"{episode_slug}.md")
        out = out_dir / f"prueba-{episode_slug}.mp3"
        engine = generate_audio.synthesize(episode["body"], out)
        minutes = generate_audio.duration_seconds(out) / 60
        print(f"::notice::{engine} - {minutes:.1f} min - {out.stat().st_size // 1024} KB")
        if not engine.startswith("Google"):
            errors.append("Se usó edge-tts en lugar de Google")
        files.append(str(out))
    text = sample_text() if VOICES and not episode_slug else ""
    for voice in VOICES if not episode_slug else []:
        out = out_dir / f"muestra-{voice}.mp3"
        try:
            synthesize(text, voice, out)
            files.append(str(out))
            print(f"OK {voice}")
        except Exception as error:  # noqa: BLE001
            errors.append(str(error))
            print(f"::error::{str(error).replace(chr(10), ' ')}")

    if files:
        exists = subprocess.run(["gh", "release", "view", TAG], capture_output=True).returncode == 0
        if not exists:
            subprocess.run(
                ["gh", "release", "create", TAG, "--prerelease", "--latest=false",
                 "--title", "Muestras de voces", "--notes", "Muestras para comparar voces de TTS."],
                check=True,
            )
        subprocess.run(["gh", "release", "upload", TAG, *files, "--clobber"], check=True)
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
