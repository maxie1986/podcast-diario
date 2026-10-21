# Veinte Minutos

Podcast diario de unos 20 minutos sobre un tema distinto cada día.

- **Feed para apps de podcasts:** https://maxie1986.github.io/podcast-diario/feed.xml
- **Página con los episodios:** https://maxie1986.github.io/podcast-diario/

## Cómo funciona

1. Una tarea programada escribe un guion en `episodes/` siguiendo [GUIA.md](GUIA.md) y lo pushea a `main`.
2. La Action `.github/workflows/podcast.yml` convierte a MP3 los episodios nuevos (`scripts/generate_audio.py`) y publica cada uno como un release `ep-*`.
3. La misma Action regenera `feed.xml` e `index.html` a partir de los releases (`scripts/build_feed.py`) y los publica en GitHub Pages.

Los MP3 se guardan como assets de releases, así el repo no crece con archivos de audio. Al publicar, los últimos 30 se copian al sitio de Pages (`audio/`) y el feed apunta ahí: GitHub sirve los assets de releases como `application/octet-stream` y Apple Podcasts no los reproduce.

## Voz

Por defecto usa Google Cloud Text-to-Speech con la voz `es-US-Chirp3-HD-Charon` (secret `GOOGLE_TTS_API_KEY`; capa gratuita de 1 millón de caracteres por mes en voces Chirp 3 HD). Si Google falla, cae a [edge-tts](https://github.com/rany2/edge-tts). Las voces se cambian sin tocar código con variables del repo (Settings → Secrets and variables → Actions → Variables):

| Variable | Default | Ejemplo |
|---|---|---|
| `GOOGLE_VOICE` | `es-US-Chirp3-HD-Charon` | `es-US-Chirp3-HD-Kore` |
| `EDGE_VOICE` | `es-AR-TomasNeural` | `es-AR-ElenaNeural` |
| `EDGE_RATE` | `+0%` | `+8%` |

Para comparar voces o probar un episodio completo sin tocar el feed: Actions → Muestras de voces → Run workflow.

## Regenerar un episodio

Borrar el release `ep-<nombre>` y su tag, y correr la Action a mano (Actions → Generar episodio y publicar feed → Run workflow).
