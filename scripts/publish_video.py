import os
import sys
import json
import urllib.parse
import urllib.request
from datetime import datetime

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
STATE_PATH = os.path.join(DIR_PATH, "..", "state", "published.json")
os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)

def load_env():
    env = dict(os.environ)
    for candidate in [os.path.join(DIR_PATH, ".env"), os.path.join(DIR_PATH, "..", ".env")]:
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

# -------------------------------------------------------------
# 1. YOUTUBE UPLOAD (Direct YouTube Data API v3)
# -------------------------------------------------------------
def get_yt_access_token():
    refresh_token = ENV.get("YT_REFRESH_TOKEN")
    client_id = ENV.get("GOOGLE_CLIENT_ID")
    client_secret = ENV.get("GOOGLE_CLIENT_SECRET")
    
    if not refresh_token:
        raise ValueError("YT_REFRESH_TOKEN belum ada di .env")
        
    data = urllib.parse.urlencode({
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "refresh_token"
    }).encode("utf-8")
    
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode())
        return res.get("access_token")

def upload_to_youtube(video_path, title, description, tags=None):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"File video tidak ditemukan: {video_path}")
        
    token = get_yt_access_token()
    file_size = os.path.getsize(video_path)
    
    clean_title = title.replace("<", "").replace(">", "").strip()[:100]
    clean_desc = description.replace("<", "").replace(">", "").strip()[:5000]
    
    snippet = {
        "title": clean_title,
        "description": clean_desc,
        "categoryId": "26", # Howto & Style / Wellness
        "defaultLanguage": "id"
    }
    if tags:
        snippet["tags"] = tags
        
    meta = {
        "snippet": snippet,
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False
        }
    }
    
    init_req = urllib.request.Request(
        "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
        data=json.dumps(meta).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Upload-Content-Type": "video/mp4",
            "X-Upload-Content-Length": str(file_size)
        },
        method="POST"
    )
    with urllib.request.urlopen(init_req) as init_resp:
        upload_url = init_resp.headers.get("Location")
        
    if not upload_url:
        raise ValueError("YouTube tidak mengembalikan upload URL resumable")
        
    print(f"[YouTube] Mengunggah Shorts ({file_size / (1024*1024):.2f} MB)...")
    
    chunk_size = 8 * 1024 * 1024
    with open(video_path, "rb") as vf:
        offset = 0
        video_id = None
        while offset < file_size:
            chunk = vf.read(min(chunk_size, file_size - offset))
            n = len(chunk)
            
            req = urllib.request.Request(
                upload_url,
                data=chunk,
                headers={
                    "Content-Type": "video/mp4",
                    "Content-Length": str(n),
                    "Content-Range": f"bytes {offset}-{offset + n - 1}/{file_size}"
                },
                method="PUT"
            )
            try:
                with urllib.request.urlopen(req) as resp:
                    if resp.status in [200, 201]:
                        res_json = json.loads(resp.read().decode())
                        video_id = res_json.get("id")
                        break
            except urllib.error.HTTPError as e:
                if e.code == 308:
                    pass
                else:
                    raise e
            offset += n
            
    if not video_id:
        raise RuntimeError("Upload YouTube selesai tetapi video ID tidak ditemukan")
        
    yt_url = f"https://youtube.com/shorts/{video_id}"
    print(f"[YouTube] ✅ BERHASIL TAYANG -> {yt_url}")
    return {"platform": "youtube", "ok": True, "videoId": video_id, "url": yt_url}

# -------------------------------------------------------------
# 2. ZERNIO UPLOAD (TikTok & Instagram Reels)
# -------------------------------------------------------------
def upload_to_zernio(video_path, caption):
    z_key = ENV.get("ZERNIO_API_KEY")
    tiktok_id = ENV.get("TIKTOK_ACCOUNT_ID")
    ig_id = ENV.get("INSTAGRAM_ACCOUNT_ID")
    
    if not z_key:
        raise ValueError("ZERNIO_API_KEY belum diset")
        
    file_size = os.path.getsize(video_path)
    file_name = os.path.basename(video_path)
    
    # 1. Presign R2 upload URL
    presign_req = urllib.request.Request(
        "https://api.zernio.com/v1/media/presign",
        data=json.dumps({
            "filename": file_name,
            "contentType": "video/mp4",
            "size": file_size
        }).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {z_key}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    with urllib.request.urlopen(presign_req) as p_resp:
        presign_data = json.loads(p_resp.read().decode())
        upload_url = presign_data.get("uploadUrl")
        public_url = presign_data.get("publicUrl")
        
    if not upload_url or not public_url:
        raise ValueError(f"Gagal mendapatkan presigned URL Zernio: {presign_data}")
        
    print(f"[Zernio] Mengunggah media binary ({file_size / (1024*1024):.2f} MB)...")
    with open(video_path, "rb") as f:
        media_bytes = f.read()
        
    put_req = urllib.request.Request(
        upload_url,
        data=media_bytes,
        headers={
            "Content-Type": "video/mp4"
        },
        method="PUT"
    )
    with urllib.request.urlopen(put_req) as put_resp:
        if put_resp.status not in [200, 204]:
            raise RuntimeError(f"Gagal upload binary ke R2: status {put_resp.status}")
            
    print("[Zernio] Binary berhasil terunggah ke Cloudflare R2.")
    
    # 2. Buat Post ke TikTok & Instagram
    platforms = []
    if tiktok_id:
        platforms.append({"platform": "tiktok", "accountId": tiktok_id})
    if ig_id:
        platforms.append({"platform": "instagram", "accountId": ig_id})
        
    post_payload = {
        "title": caption.split("\n")[0][:80],
        "content": caption,
        "mediaItems": [{"type": "video", "url": public_url}],
        "platforms": platforms,
        "publishNow": True
    }
    
    post_req = urllib.request.Request(
        "https://api.zernio.com/v1/posts",
        data=json.dumps(post_payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {z_key}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    with urllib.request.urlopen(post_req) as post_resp:
        post_res = json.loads(post_resp.read().decode())
        post_obj = post_res.get("post") or post_res.get("data") or post_res
        post_id = post_obj.get("_id") or post_obj.get("id")
        
    print(f"[Zernio] ✅ POST BERHASIL DIBUAT (ID: {post_id})")
    return {"platform": "zernio", "ok": True, "postId": post_id, "data": post_obj}

# -------------------------------------------------------------
# 3. MAIN RUNNER
# -------------------------------------------------------------
def main():
    import argparse
    parser = argparse.ArgumentParser(description="Multi-platform publisher for DITA-03")
    parser.add_argument("--day", type=int, default=None, help="Day index to publish")
    parser.add_argument("--video", type=str, default=None, help="Custom video path")
    args = parser.parse_args()

    day_num = args.day
    campaign_state_file = os.path.join(DIR_PATH, "..", "state", "campaign_state.json")
    if day_num is None:
        if os.path.exists(campaign_state_file):
            try:
                with open(campaign_state_file, "r", encoding="utf-8") as f:
                    cs = json.load(f)
                    day_num = cs.get("next_day") or (cs.get("active_day", 1) + 1)
            except Exception:
                day_num = 1
        else:
            day_num = 1

    pad_day = str(day_num).zfill(3)
    packet_path = os.path.join(DIR_PATH, "..", "curriculum", f"content_packet_day_{pad_day}.json")
    if not os.path.exists(packet_path):
        packet_path = os.path.join(DIR_PATH, "curriculum", f"content_packet_day_{pad_day}.json")

    if not os.path.exists(packet_path):
        print(f"[ERROR] Packet file not found: {packet_path}")
        sys.exit(1)

    with open(packet_path, "r", encoding="utf-8") as pf:
        packet = json.load(pf)

    video_path = args.video
    if not video_path:
        candidates = [
            os.path.join(DIR_PATH, "..", "output", f"dita_wellness_day_{pad_day}_compressed.mp4"),
            os.path.join(DIR_PATH, "..", "output", f"dita_wellness_day_{pad_day}_master.mp4"),
            os.path.join(DIR_PATH, "output", f"dita_wellness_day_{pad_day}_compressed.mp4"),
            os.path.join(DIR_PATH, "output", f"dita_wellness_day_{pad_day}_master.mp4"),
        ]
        for c in candidates:
            if os.path.exists(c) and os.path.getsize(c) > 500000:
                video_path = c
                break

    if not video_path or not os.path.exists(video_path):
        print(f"[ERROR] Video file not found for Day {day_num}. Run render-video.ts first.")
        sys.exit(1)

    print(f"Target Video: {video_path}")
    dist_meta = packet.get("social_fleet_distribution_metadata", {})
    yt_title = dist_meta.get("youtube_shorts_title") or f"{packet.get('metadata', {}).get('cycle_theme', 'Gentle Wellness')} #Shorts"
    z_caption = dist_meta.get("caption_instagram_tiktok") or packet.get("verbatim_script_master", {}).get("full_spoken_text_id", "")
    yt_desc = f"{z_caption}\n\n#Shorts #DitaWellness #GentleWellness #BiohackingIndonesia #SainsKesehatan"
    tags = ["DitaWellness", "Biohacking", "RitmeSirkadian", "Kesehatan", "DeepSleep", "GentleWellness", "Shorts"]

    results = {}
    
    # 1. Dispatch YouTube
    try:
        yt_res = upload_to_youtube(video_path, yt_title, yt_desc, tags)
        results["youtube"] = yt_res
    except Exception as e:
        print(f"[YouTube] ERROR: {e}")
        results["youtube"] = {"ok": False, "error": str(e)}
        
    # 2. Dispatch Zernio (TikTok + IG)
    try:
        z_res = upload_to_zernio(video_path, z_caption)
        results["zernio"] = z_res
    except Exception as e:
        print(f"[Zernio] ERROR: {e}")
        results["zernio"] = {"ok": False, "error": str(e)}
        
    # Save Published State
    history = []
    if os.path.exists(STATE_PATH):
        try:
            with open(STATE_PATH, "r", encoding="utf-8") as f:
                history = json.load(f)
        except Exception:
            history = []
            
    history.append({
        "day": day_num,
        "published_at": datetime.now().isoformat(),
        "video": os.path.basename(video_path),
        "results": results
    })
    
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
        
    print(f"\n[STATE] History publikasi tersimpan di {STATE_PATH}")
    print("============================================================")
    print(f"  STATUS PUBLIKASI DAY {pad_day} (@ditawellness)")
    print("============================================================")
    for k, v in results.items():
        print(f" - {k.upper()}: {'✅ SUCCESS' if v.get('ok') else '❌ FAILED'} -> {v.get('url') or v.get('postId') or v.get('error')}")

if __name__ == "__main__":
    main()
