import os
import sys
import json
import random
import urllib.request
import urllib.parse
from datetime import datetime

def load_env():
    env = {}
    env_file = ".env"
    if os.path.exists(env_file):
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip()
    return env

ENV = load_env()
PEXELS_KEY = os.environ.get("PEXELS_API_KEY") or ENV.get("PEXELS_API_KEY")
USED_ASSETS_FILE = "state/used_broll_assets.json"

DEFAULT_SCENES = [
    {"scene_id": "SCENE_01", "timeStart": 0, "timeEnd": 4, "query": "toddler listening whispering"},
    {"scene_id": "SCENE_02", "timeStart": 4, "timeEnd": 8, "query": "mother kneeling gentle talking child"},
    {"scene_id": "SCENE_03", "timeStart": 8, "timeEnd": 14, "query": "child playing wooden blocks peaceful"},
    {"scene_id": "SCENE_04", "timeStart": 14, "timeEnd": 20, "query": "calm human brain neural network"},
    {"scene_id": "SCENE_05", "timeStart": 20, "timeEnd": 27, "query": "parent whispering secret to child"},
    {"scene_id": "SCENE_06", "timeStart": 27, "timeEnd": 33, "query": "parent and toddler smiling together"},
    {"scene_id": "SCENE_07", "timeStart": 33, "timeEnd": 43, "query": "mother holding toddler hands lovingly"},
    {"scene_id": "SCENE_08", "timeStart": 43, "timeEnd": 50, "query": "happy toddler laughing home"},
    {"scene_id": "SCENE_09", "timeStart": 50, "timeEnd": 58, "query": "peaceful family cozy living room"}
]

def load_used_assets():
    if os.path.exists(USED_ASSETS_FILE):
        try:
            with open(USED_ASSETS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return set(data.get("used_ids", [])), data.get("history", [])
        except Exception as e:
            print(f"[B-Roll] Gagal membaca {USED_ASSETS_FILE}: {e}")
    return set(), []

def save_used_assets(used_ids_set, history_list):
    os.makedirs(os.path.dirname(USED_ASSETS_FILE), exist_ok=True)
    try:
        with open(USED_ASSETS_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "total_used": len(used_ids_set),
                "last_updated": datetime.now().isoformat(),
                "used_ids": list(used_ids_set),
                "history": history_list[-300:]
            }, f, indent=2)
    except Exception as e:
        print(f"[B-Roll] Gagal menyimpan {USED_ASSETS_FILE}: {e}")

def search_pexels_video(query, used_ids_set, max_pages=3):
    if not PEXELS_KEY:
        print("[B-Roll] Warning: PEXELS_API_KEY tidak ditemukan di environment.")
        return None, None

    pages_to_check = list(range(1, max_pages + 1))
    random.shuffle(pages_to_check)

    for page in pages_to_check:
        url = (
            f"https://api.pexels.com/videos/search?"
            f"query={urllib.parse.quote(query)}&orientation=portrait&per_page=15&page={page}"
        )
        req = urllib.request.Request(url, headers={
            "Authorization": PEXELS_KEY,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })

        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode())
                videos = data.get("videos", [])
                if not videos:
                    continue

                fresh_videos = [v for v in videos if v.get("id") not in used_ids_set]
                if not fresh_videos:
                    continue

                for v in fresh_videos:
                    vid_id = v.get("id")
                    files = v.get("video_files", [])

                    # 1. Prioritaskan tepat 720x1280 portrait
                    for f in files:
                        if f.get("width") == 720 and f.get("height") == 1280 and f.get("link"):
                            return vid_id, f.get("link")

                    # 2. Atau format portrait lain (width < height <= 1920)
                    for f in files:
                        w = f.get("width", 0)
                        h = f.get("height", 0)
                        if w > 0 and h > 0 and w < h and h <= 1920 and f.get("link"):
                            return vid_id, f.get("link")

        except Exception as e:
            print(f"[B-Roll] Pexels search query '{query}' (page {page}) error: {e}")

    return None, None

def download_file(url, out_path):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    })
    with urllib.request.urlopen(req, timeout=25) as resp:
        with open(out_path, "wb") as f:
            f.write(resp.read())

def main():
    packet_path = sys.argv[1] if len(sys.argv) > 1 else "curriculum/content_packet_day_001.json"
    out_dir = "public/broll"
    os.makedirs(out_dir, exist_ok=True)

    used_ids_set, history_list = load_used_assets()
    print(f"[B-Roll] Terdaftar {len(used_ids_set)} ID video lama dalam blacklist anti-dejavu.")

    scenes = DEFAULT_SCENES
    day_num = 1

    if os.path.exists(packet_path):
        with open(packet_path, "r", encoding="utf-8") as f:
            pkt = json.load(f)
            day_num = pkt.get("metadata", {}).get("day_number", 1)
            broll_cues = pkt.get("production_prompts_for_fullmontage", {}).get("broll_queries", [])
            if broll_cues:
                scenes = broll_cues

    manifest = []
    print(f"[B-Roll] Mempersiapkan {len(scenes)} adegan sinematik unik untuk Day {day_num}...")

    fallback_pool = [
        "parent whispering ear toddler cozy",
        "toddler playing sensory toys floor",
        "mother listening smiling child room",
        "father playing with toddler laughing",
        "little hands building colorful wooden blocks",
        "warm sunlit living room toddler gentle moment",
        "parent holding child hand walking slowly",
        "toddler hugging soft teddy bear calm",
        "cozy nursery playroom soft morning light"
    ]

    for i, sc in enumerate(scenes, 1):
        scene_id = sc.get("scene_id", f"SCENE_{i:02d}")
        query = sc.get("query", "parenting toddler")
        filename = f"broll_{i}.mp4"
        file_path = os.path.join(out_dir, filename)
        web_path = f"broll/{filename}"

        print(f"[B-Roll] Scene {i}/{len(scenes)}: '{query}' ({sc.get('timeStart')}s -> {sc.get('timeEnd')}s)...")

        vid_id, dl_url = search_pexels_video(query, used_ids_set)

        if not dl_url:
            alt_query = fallback_pool[(i - 1) % len(fallback_pool)]
            print(f"   [!] Kueri '{query}' habis atau nihil video baru. Mencoba kueri variasi: '{alt_query}'...")
            vid_id, dl_url = search_pexels_video(alt_query, used_ids_set)

        if dl_url and vid_id:
            try:
                download_file(dl_url, file_path)
                size_mb = os.path.getsize(file_path) / (1024 * 1024)
                print(f"   ✓ Sukses diunduh -> {filename} (ID: {vid_id}, {size_mb:.2f} MB) [100% FRESH]")

                used_ids_set.add(vid_id)
                history_list.append({
                    "day": day_num,
                    "scene_id": scene_id,
                    "video_id": vid_id,
                    "query": query,
                    "downloaded_at": datetime.now().isoformat()
                })

                manifest.append({
                    "scene_id": scene_id,
                    "timeStart": sc.get("timeStart", 0),
                    "timeEnd": sc.get("timeEnd", 60),
                    "videoSrc": web_path,
                    "query": query,
                    "pexels_id": vid_id
                })
            except Exception as e:
                print(f"   ✗ Gagal mengunduh URL ({dl_url}): {e}")
        else:
            print(f"   - Melewati video {i} (menggunakan fallback visual Remotion)")

    save_used_assets(used_ids_set, history_list)

    manifest_file = "public/broll_manifest.json"
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"[B-Roll] Selesai. {len(manifest)} klip 100% UNIK tersimpan di manifest -> {manifest_file}")

if __name__ == "__main__":
    main()
