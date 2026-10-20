"""Genera _site/feed.xml (RSS de podcast) e index.html a partir de los releases ep-*."""

import json
import os
import shutil
import subprocess
from datetime import datetime
from email.utils import format_datetime
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"

REPO = os.environ["GITHUB_REPOSITORY"]
OWNER, NAME = REPO.split("/")
BASE_URL = f"https://{OWNER}.github.io/{NAME}/"

TITLE = "Veinte Minutos"
DESCRIPTION = "Un tema distinto cada día, contado en unos veinte minutos."
AUTHOR = OWNER
MAX_EPISODES = 30  # unos 220 MB; Pages admite hasta 1 GB por sitio


def releases() -> list[dict]:
    result = subprocess.run(
        ["gh", "api", f"repos/{REPO}/releases", "--paginate"],
        capture_output=True, text=True, check=True,
    )
    items = []
    for release in json.loads(result.stdout.replace("][", ",")):
        if not release["tag_name"].startswith("ep-"):
            continue
        assets = [a for a in release["assets"] if a["name"].endswith(".mp3")]
        if not assets:
            continue
        try:
            notes = json.loads(release.get("body") or "{}")
        except json.JSONDecodeError:
            notes = {}
        items.append({"release": release, "asset": assets[0], "notes": notes})
    items.sort(key=lambda i: i["release"]["published_at"], reverse=True)
    return items


def hms(seconds: int) -> str:
    return f"{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"


def build() -> None:
    SITE.mkdir(exist_ok=True)
    cover = ROOT / "assets" / "cover.png"
    if cover.exists():
        shutil.copy(cover, SITE / "cover.png")

    # Apple Podcasts rechaza los assets de releases (se sirven como
    # application/octet-stream). Se copian los últimos MAX_EPISODES MP3 al
    # sitio de Pages, que los sirve como audio/mpeg con soporte de rangos.
    episodes = releases()[:MAX_EPISODES]
    audio_dir = SITE / "audio"
    audio_dir.mkdir(exist_ok=True)
    entries, rows = [], []
    for item in episodes:
        release, asset, notes = item["release"], item["asset"], item["notes"]
        subprocess.run(
            ["gh", "release", "download", release["tag_name"], "-R", REPO,
             "-p", asset["name"], "-D", str(audio_dir), "--clobber"],
            check=True,
        )
        audio_url = f"{BASE_URL}audio/{quote(asset['name'])}"
        published = datetime.fromisoformat(release["published_at"].replace("Z", "+00:00"))
        description = notes.get("description", "")
        duration = int(notes.get("duration", 0))
        entries.append(f"""    <item>
      <title>{escape(release["name"])}</title>
      <description>{escape(description)}</description>
      <guid isPermaLink="false">{escape(release["tag_name"])}</guid>
      <pubDate>{format_datetime(published)}</pubDate>
      <enclosure url="{escape(audio_url)}" length="{asset["size"]}" type="audio/mpeg"/>
      <itunes:duration>{hms(duration)}</itunes:duration>
      <itunes:explicit>false</itunes:explicit>
    </item>""")
        rows.append(
            f'<li><strong>{escape(release["name"])}</strong> '
            f'<span>{published:%d/%m/%Y} · {duration // 60} min</span>'
            f'<p>{escape(description)}</p>'
            f'<audio controls preload="none" src="{escape(audio_url)}"></audio></li>'
        )

    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{TITLE}</title>
    <link>{BASE_URL}</link>
    <atom:link href="{BASE_URL}feed.xml" rel="self" type="application/rss+xml"/>
    <description>{DESCRIPTION}</description>
    <language>es-ar</language>
    <itunes:author>{AUTHOR}</itunes:author>
    <itunes:image href="{BASE_URL}cover.png"/>
    <itunes:category text="Education"/>
    <itunes:explicit>false</itunes:explicit>
{chr(10).join(entries)}
  </channel>
</rss>
"""
    (SITE / "feed.xml").write_text(feed, encoding="utf-8")

    page = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<link rel="alternate" type="application/rss+xml" href="feed.xml">
<style>
body{{font-family:system-ui,sans-serif;max-width:680px;margin:0 auto;padding:24px 16px;line-height:1.5}}
ul{{list-style:none;padding:0}} li{{padding:16px 0;border-bottom:1px solid #ddd}}
span{{color:#666;font-size:.9em}} audio{{width:100%}} code{{word-break:break-all}}
</style></head><body>
<h1>{TITLE}</h1><p>{DESCRIPTION}</p>
<p>Feed para tu app de podcasts: <code>{BASE_URL}feed.xml</code></p>
<ul>{"".join(rows)}</ul>
</body></html>
"""
    (SITE / "index.html").write_text(page, encoding="utf-8")
    print(f"Feed con {len(episodes)} episodios.")


if __name__ == "__main__":
    build()
