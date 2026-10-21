import os
import sys
import json
import urllib.request
import urllib.parse
import subprocess
from datetime import datetime

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(DIR_PATH)
STATE_DIR = os.path.join(ROOT_DIR, "state")
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
BROLL_DIR = os.path.join(PUBLIC_DIR, "broll")
USED_ASSETS_FILE = os.path.join(STATE_DIR, "used_broll_assets.json")

def load_env():
    env = dict(os.environ)
    for candidate in [os.path.join(DIR_PATH, ".env"), os.path.join(ROOT_DIR, ".env")]:
        if os.path.exists(candidate):
            with open(candidate, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        if k.strip() not in env:
                            env[k.strip()] = v.strip()
    return env

ENV = load_env()
PEXELS_KEY = ENV.get("PEXELS_API_KEY")

def load_used_assets():
    if os.path.exists(USED_ASSETS_FILE):
        try:
            with open(USED_ASSETS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return set(data.get("used_ids", [])), data.get("history", [])
        except Exception as e:
            print(f"[B-Roll] Gagal membaca used assets: {e}")
    return set(), []

def save_used_assets(used_ids_set, history_list):
    os.makedirs(STATE_DIR, exist_ok=True)
    try:
        with open(USED_ASSETS_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "total_used": len(used_ids_set),
                "last_updated": datetime.now().isoformat(),
                "used_ids": list(used_ids_set),
                "history": history_list[-500:]
            }, f, indent=2)
    except Exception as e:
        print(f"[B-Roll] Gagal menyimpan used assets: {e}")

def derive_queries_for_day(day_num, packet):
    core_topic = (packet.get("scientific_research_dossier", {}).get("core_topic") or "").lower()
    
    # Specialized Topic Mapping
    if any(w in core_topic for w in ["kopi", "kafein", "adenosin"]):
        return [
            "hot coffee cup steam morning",
            "tired waking up bed morning",
            "exhausted office worker afternoon desk",
            "drinking fresh water morning glass",
            "roasted coffee beans macro aesthetic"
        ]
    elif any(w in core_topic for w in ["mandi", "hangat", "suhu inti", "air hangat"]):
        return [
            "running bath water steam bathtub",
            "cozy bedroom candlelight night",
            "warm water soothing drops bath",
            "stretching bedroom night dim lamp",
            "sleeping peacefully cozy bed dark"
        ]
    elif any(w in core_topic for w in ["senja", "sunset", "langit senja", "sore"]):
        return [
            "sunset golden hour sky clouds",
            "person looking sunset horizon silhouette",
            "orange pink dusk clouds timelapse",
            "evening walk park nature silhouette",
            "night sky stars peaceful twilight"
        ]
    elif any(w in core_topic for w in ["makan", "puasa", "sebelum tidur", "lambung", "dinner"]):
        return [
            "dinner table food evening plate",
            "person sleeping tossing turning uncomfortable",
            "digestion stomach herbal tea cup",
            "drinking warm chamomile tea night",
            "deep calm sleep bedroom night"
        ]
    elif any(w in core_topic for w in ["blue light", "layar", "kacamata", "hp", "gadget", "ponsel"]):
        return [
            "blue light smartphone face dark room",
            "person wearing glasses looking laptop screen",
            "dimming lamp warm amber light night",
            "turning off phone bedtime aesthetic",
            "peaceful sleep dark bedroom eye mask"
        ]
    elif any(w in core_topic for w in ["jetlag", "bangun siang", "minggu", "jam alarm", "alarm"]):
        return [
            "alarm clock ringing morning snooze",
            "waking up late noon sunlight bed",
            "tired groggy person walking morning",
            "morning sunlight routine stretching",
            "nature walking morning sunrise fresh"
        ]
    elif any(w in core_topic for w in ["usus", "gut", "kembung", "bloating", "mikrobiom", "fermentasi"]):
        return [
            "healthy fermented food kefir yogurt",
            "fresh green salad vegetable fiber",
            "herbal tea pouring cup steam",
            "drinking kombucha healthy glass",
            "clean aesthetic kitchen herbs botanical"
        ]
    elif any(w in core_topic for w in ["gula darah", "glukosa", "insulin", "manis", "karbohidrat"]):
        return [
            "delicious breakfast avocado eggs savory",
            "eating fresh salad greens first",
            "walking outside city park nature",
            "drinking water lemon morning",
            "calm zen nature sunlight morning"
        ]
    elif any(w in core_topic for w in ["kortisol", "stres", "stress", "cemas", "anxiety", "vagus"]):
        return [
            "stressed person laptop deep breath",
            "deep breathing outdoors hands chest",
            "cold water splash face morning",
            "writing gratitude journal wooden desk",
            "golden hour nature horizon serene"
        ]
    elif any(w in core_topic for w in ["hidrasi", "air putih", "elektrolit", "garam"]):
        return [
            "pouring clear water glass macro drops",
            "drinking fresh water sunny morning",
            "fresh lemon slices water pitcher",
            "gentle ocean waves shoreline clear",
            "morning sun rays through green leaves"
        ]
    elif any(w in core_topic for w in ["tidur", "sleep", "insomnia", "nyenyak", "melatonin"]):
        return [
            "dark cozy bedroom ambient soft light",
            "stretching bed night relaxed silhouette",
            "pouring hot chamomile tea cup",
            "candle flame flickering dark serene",
            "peaceful sleep in cozy white bed"
        ]
    
    # General Wellness & Zen Aesthetic Rotation (Deterministic per day)
    general_pool = [
        "minimalist botanical nature aesthetic",
        "morning window sunlight calm aesthetic",
        "herbal tea pouring steam cup macro",
        "forest trees sunlight serene walk",
        "zen stone water garden peaceful",
        "hands writing journal aesthetic desk",
        "green tea matcha whisking bamboo",
        "calm water ripples slow motion aesthetic",
        "warm knit blanket reading book cozy",
        "morning mist rising mountain forest"
    ]
    offset = (day_num * 3) % len(general_pool)
    return [general_pool[(offset + i) % len(general_pool)] for i in range(5)]

def search_pexels_video(query, used_ids_set):
    if not PEXELS_KEY:
        print("[B-Roll] ERROR: PEXELS_API_KEY tidak ditemukan.")
        return None, None

    url = (
        f"https://api.pexels.com/videos/search?"
        f"query={urllib.parse.quote(query)}&orientation=portrait&per_page=12"
    )
    req = urllib.request.Request(url, headers={
        "Authorization": PEXELS_KEY,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    })

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            videos = data.get("videos", [])
            for v in videos:
                vid_id = v.get("id")
                if vid_id in used_ids_set:
                    continue

                files = v.get("video_files", [])
                # 1. Prioritas tepat 720x1280 atau 1080x1920
                for f in files:
                    w, h = f.get("width"), f.get("height")
                    if w in [720, 1080] and h in [1280, 1920] and f.get("link"):
                        return vid_id, f.get("link")

                # 2. Portrait umum
                for f in files:
                    w, h = f.get("width", 0), f.get("height", 0)
                    if 0 < w < h and f.get("link"):
                        return vid_id, f.get("link")
    except Exception as e:
        print(f"[B-Roll] Search error for '{query}': {e}")
    return None, None

def fetch_broll_for_day(day_num):
    day_str = f"{day_num:03d}"
    print(f"\n========================================================")
    print(f"  [ANTI-DEJAVU] FETCHING TOPIC B-ROLL FOR DAY {day_str}")
    print(f"========================================================")

    packet_file = os.path.join(ROOT_DIR, "curriculum", f"content_packet_day_{day_str}.json")
    if not os.path.exists(packet_file):
        print(f"[B-Roll] ERROR: Packet not found: {packet_file}")
        return False

    with open(packet_file, "r", encoding="utf-8") as f:
        packet = json.load(f)

    topic = packet.get("scientific_research_dossier", {}).get("core_topic")
    print(f"Topic: {topic}")

    queries = derive_queries_for_day(day_num, packet)
    print(f"Derived Queries ({len(queries)}):")
    for idx, q in enumerate(queries, 1):
        print(f"  [{idx}] {q}")

    day_broll_dir = os.path.join(PUBLIC_DIR, "broll", f"day_{day_str}")
    os.makedirs(day_broll_dir, exist_ok=True)

    used_ids, history = load_used_assets()
    downloaded_scenes = []

    for idx, query in enumerate(queries, 1):
        sc_num = f"{idx:02d}"
        dest_mp4 = os.path.join(day_broll_dir, f"scene_{sc_num}.mp4")

        # Skip if already exists and valid
        if os.path.exists(dest_mp4) and os.path.getsize(dest_mp4) > 300000:
            print(f"  -> Scene {sc_num} already downloaded ({os.path.getsize(dest_mp4) / 1024:.1f} KB).")
            downloaded_scenes.append(dest_mp4)
            continue

        vid_id, link = search_pexels_video(query, used_ids)
        if not link:
            fallback_query = "minimalist botanical nature morning aesthetic"
            vid_id, link = search_pexels_video(fallback_query, used_ids)

        if not link:
            print(f"  [FAIL] Could not find video for Scene {sc_num} ('{query}')")
            continue

        print(f"  -> Downloading Scene {sc_num} (ID: {vid_id}) for '{query}'...")
        temp_dest = os.path.join(day_broll_dir, f"temp_{sc_num}.mp4")
        
        req = urllib.request.Request(link, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp, open(temp_dest, "wb") as f_out:
            f_out.write(resp.read())

        # Normalize with ffmpeg to 720x1280 @ 24fps libx264
        cmd_norm = [
            "ffmpeg", "-y", "-i", temp_dest,
            "-vf", "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280",
            "-c:v", "libx264", "-crf", "22", "-preset", "veryfast", "-an",
            dest_mp4
        ]
        try:
            subprocess.run(cmd_norm, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if os.path.exists(temp_dest):
                os.remove(temp_dest)
        except Exception:
            if os.path.exists(temp_dest):
                if os.path.exists(dest_mp4):
                    os.remove(dest_mp4)
                os.rename(temp_dest, dest_mp4)

        size_kb = os.path.getsize(dest_mp4) / 1024
        print(f"     ✅ Saved: scene_{sc_num}.mp4 ({size_kb:.1f} KB)")
        used_ids.add(vid_id)
        history.append({
            "day": day_num,
            "scene": sc_num,
            "video_id": vid_id,
            "query": query,
            "downloaded_at": datetime.now().isoformat()
        })
        downloaded_scenes.append(dest_mp4)

    save_used_assets(used_ids, history)
    print(f"\n[B-Roll] Day {day_str} completed with {len(downloaded_scenes)}/5 distinct scenes in {day_broll_dir}!")
    return len(downloaded_scenes) >= 4

if __name__ == "__main__":
    day = 2
    for idx, arg in enumerate(sys.argv):
        if arg == "--day" and idx + 1 < len(sys.argv):
            day = int(sys.argv[idx + 1])
        elif arg.isdigit() and idx > 0:
            day = int(arg)
    fetch_broll_for_day(day)
