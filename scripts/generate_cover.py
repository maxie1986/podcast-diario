"""Portada de cada episodio: ilustración generada con Gemini y el título encima.

Si no hay API key o la generación falla, arma una portada de plantilla con el
título sobre un degradé de color, así el episodio nunca se queda sin imagen.
"""

import base64
import hashlib
import io
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "assets" / "fonts" / "ArchivoBlack.ttf"
SIZE = 1400
MARGIN = 96
YELLOW = (242, 183, 5)

KEY = (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_TTS_API_KEY") or "").strip()
IMAGE_MODEL = os.environ.get("IMAGE_MODEL", "gemini-2.5-flash-image").strip()

PALETTES = [
    ((18, 32, 47), (31, 86, 115)),
    ((40, 22, 58), (122, 52, 98)),
    ((14, 46, 38), (36, 120, 92)),
    ((58, 30, 18), (166, 84, 38)),
    ((22, 26, 60), (66, 82, 168)),
    ((52, 18, 24), (150, 44, 56)),
]

PROMPT = """Create a square editorial illustration to be used as the cover art of a podcast episode.

Episode title: {title}
Episode summary: {description}
Topic: {topic}

Style: modern, vivid editorial illustration with rich colors, soft lighting and bold simple shapes; one clear, recognizable central subject that represents the topic; uncluttered background. Keep the bottom third of the image calm and fairly dark, because the title will be overlaid there.
Strictly no text, letters, numbers, captions, logos, watermarks, trademarks or copyrighted characters anywhere in the image."""


def font(size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(str(FONT), size)
    except OSError:
        return ImageFont.truetype("DejaVuSans-Bold.ttf", size)


def gemini_illustration(episode: dict) -> Image.Image:
    prompt = PROMPT.format(
        title=episode.get("title", ""),
        description=episode.get("description", ""),
        topic=episode.get("topic", ""),
    )
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {"aspectRatio": "1:1"},
        },
    }).encode("utf-8")
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
           f"{IMAGE_MODEL}:generateContent?key={KEY}")
    request = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                data = json.load(response)
            break
        except urllib.error.HTTPError as error:
            detail = error.read().decode()[:400]
            if (error.code < 500 and error.code != 429) or attempt == 2:
                raise RuntimeError(f"Gemini HTTP {error.code}: {detail}") from error
        time.sleep(10 * (attempt + 1))
    for candidate in data.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                return Image.open(io.BytesIO(base64.b64decode(inline["data"]))).convert("RGB")
    raise RuntimeError(f"Gemini no devolvió imagen: {json.dumps(data)[:400]}")


def template_background(episode: dict) -> Image.Image:
    seed = hashlib.md5((episode.get("topic") or episode.get("title", "")).encode()).digest()[0]
    top, bottom = PALETTES[seed % len(PALETTES)]
    image = Image.new("RGB", (SIZE, SIZE))
    draw = ImageDraw.Draw(image)
    for y in range(SIZE):
        t = y / SIZE
        draw.line([(0, y), (SIZE, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(top, bottom)))
    # Un "20" grande y tenue como marca de agua de la serie, en la mitad de arriba.
    mark = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    ImageDraw.Draw(mark).text((SIZE - 70, 60), "20", font=font(560), anchor="ra",
                              fill=(255, 255, 255, 22))
    return Image.alpha_composite(image.convert("RGBA"), mark).convert("RGB")


def square(image: Image.Image) -> Image.Image:
    side = min(image.size)
    left, top = (image.width - side) // 2, (image.height - side) // 2
    return image.crop((left, top, left + side, top + side)).resize((SIZE, SIZE), Image.LANCZOS)


def wrap(draw: ImageDraw.ImageDraw, text: str, typeface, width: int) -> list[str]:
    lines, current = [], ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if draw.textlength(candidate, font=typeface) <= width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def layout_title(draw: ImageDraw.ImageDraw, title: str):
    """Elige el tamaño más grande que entre en 3 líneas (o 4 si no hay forma)."""
    width = SIZE - 2 * MARGIN
    for max_lines in (3, 4):
        for size in range(100, 54, -4):
            typeface = font(size)
            lines = wrap(draw, title, typeface, width)
            if len(lines) <= max_lines and all(draw.textlength(l, font=typeface) <= width for l in lines):
                return typeface, size, lines
    return typeface, size, lines


def compose(background: Image.Image, episode: dict) -> Image.Image:
    image = square(background).convert("RGBA")
    draw = ImageDraw.Draw(image)
    typeface, size, lines = layout_title(draw, episode.get("title", "").strip())
    line_height = int(size * 1.12)
    text_top = SIZE - MARGIN - line_height * len(lines)
    label_top = text_top - 92

    # Degradé oscuro que arranca un poco arriba del texto, para que siempre se lea.
    start = max(0, label_top - 240)
    shade = Image.new("L", (1, SIZE))
    for y in range(SIZE):
        t = 0 if y < start else (y - start) / (SIZE - start)
        shade.putpixel((0, y), int(225 * min(1, t * 1.6) ** 1.2))
    overlay = Image.new("RGBA", (SIZE, SIZE), (8, 12, 20, 255))
    overlay.putalpha(shade.resize((SIZE, SIZE)))
    image = Image.alpha_composite(image, overlay)

    draw = ImageDraw.Draw(image)
    draw.rectangle([MARGIN, label_top, MARGIN + 64, label_top + 8], fill=YELLOW)
    draw.text((MARGIN, label_top + 26), "VEINTE MINUTOS", font=font(38), fill=YELLOW)
    y = text_top
    for line in lines:
        draw.text((MARGIN, y), line, font=typeface, fill=(255, 255, 255))
        y += line_height
    return image.convert("RGB")


def make_cover(episode: dict, out: Path) -> str:
    """Genera la portada en `out` (JPG) y devuelve qué método se usó."""
    method = "plantilla"
    background = None
    if KEY:
        try:
            background = gemini_illustration(episode)
            method = f"Gemini ({IMAGE_MODEL})"
        except Exception as error:  # noqa: BLE001
            print(f"::warning::Portada con IA falló, uso plantilla: {str(error).replace(chr(10), ' ')}", file=sys.stderr)
    if background is None:
        background = template_background(episode)
    compose(background, episode).save(out, "JPEG", quality=88, optimize=True)
    return method


if __name__ == "__main__":
    # Uso: python scripts/generate_cover.py episodes/<archivo>.md salida.jpg
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from generate_audio import parse_episode

    print(make_cover(parse_episode(Path(sys.argv[1])), Path(sys.argv[2])))
