# 🌿 Dita Gentle Wellness (`@ditawellness`)

Autonomous Multi-Platform Content Factory & Production Pipeline combining **HyperFrames** (animated vector science diagrams & circadian SCN clock) and **Remotion** (cinematic ambient B-roll compositing, kinetic typography, and audio mastering).

## 🚀 Saluran Resmi
- **YouTube Shorts:** [@ditawellness](https://www.youtube.com/@ditawellness)
- **TikTok:** [@ditawellness](https://www.tiktok.com/@ditawellness)
- **Instagram Reels:** [@ditawellness](https://www.instagram.com/ditawellness)

## 🏛️ Arsitektur Teknologi
1. **HyperFrames Engine (`hyperframes_scenes/`):**
   - Renders 720x1280 @24fps subpixel vector biological animations (SCN 24h clock, photon eye stream, Cortisol vs Melatonin hormone curves) using GSAP motion path.
2. **Remotion Engine (`remotion/`):**
   - Composites ambient B-roll footage, dark vignette overlays, kinetic subtitles, and branded zen outro cards into final compressed vertical shorts (< 3.8 MB).
3. **Multi-Platform Publisher (`scripts/`):**
   - YouTube Data API v3 (Resumable chunked upload).
   - Zernio SDK (Dual upload to TikTok and Instagram Reels via Cloudflare R2).

## 📁 Struktur Repositori
- `curriculum/` — Master Kurikulum Anti-Dejavu 180 Hari (26 Minggu) & paket riset ilmiah.
- `hyperframes_scenes/` — Kode sumber komposisi HTML/SVG + GSAP HyperFrames.
- `remotion/` — Komponen React Remotion (`WellnessShorts.tsx`, `Root.tsx`).
- `scripts/` — Skrip automasi pipeline, perakitan, dan publikasi.
- `state/` — Log catatan publikasi (`published.json`) dan campaign pointer.
- `.github/workflows/` — Cron runner otomatis GitHub Actions (setiap 06:30 WIB).

## ⚡ Quick Start
```bash
# Cek status platform terhubung
python scripts/publish.py status

# Render video harian
npm run render

# Publish video
python scripts/publish_video.py
```
