import os
import sys
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta

WIB = timezone(timedelta(hours=7))

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(DIR_PATH)

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
BOT_TOKEN = ENV.get("TELEGRAM_BOT_TOKEN") or ENV.get("BOT_TOKEN")
OWNER_CHAT_ID = ENV.get("TELEGRAM_CHAT_ID") or ENV.get("OWNER_CHAT_ID")

def send_telegram(text: str) -> bool:
    if not BOT_TOKEN or not OWNER_CHAT_ID:
        print("[Telegram Reporter] BOT_TOKEN or OWNER_CHAT_ID missing, skipped sending.")
        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": OWNER_CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print("[Telegram Reporter] Report sent successfully to Telegram!")
            return True
    except Exception as e:
        print(f"[Telegram Reporter] Error sending telegram message: {e}")
        return False

def report_success(day_num: int):
    now_wib = datetime.now(WIB).strftime("%A, %d %b %Y %H:%M WIB")
    pad_day = f"{day_num:03d}"
    
    # 1. Baca packet info
    packet_path = os.path.join(ROOT_DIR, "curriculum", f"content_packet_day_{pad_day}.json")
    topic = "Gentle Wellness & Biohacking"
    pillar = "Penyejuk Hati & Fisiologi"
    if os.path.exists(packet_path):
        try:
            with open(packet_path, "r", encoding="utf-8") as pf:
                pkt = json.load(pf)
                topic = (
                    pkt.get("social_fleet_distribution_metadata", {}).get("title") or
                    pkt.get("scientific_research_dossier", {}).get("core_topic") or
                    topic
                )
                pillar = pkt.get("metadata", {}).get("topic_pillar_name") or pillar
        except Exception:
            pass

    # 2. Baca publication receipt dari state/published.json
    pub_file = os.path.join(ROOT_DIR, "state", "published.json")
    yt_url = ""
    tiktok_status = "Diproses"
    ig_status = "Diproses"
    if os.path.exists(pub_file):
        try:
            with open(pub_file, "r", encoding="utf-8") as f:
                history = json.load(f)
                for entry in reversed(history):
                    if entry.get("day") == day_num:
                        results = entry.get("results", {})
                        yt = results.get("youtube", {})
                        if yt.get("ok"):
                            yt_url = yt.get("url") or f"https://youtube.com/shorts/{yt.get('videoId')}"
                        
                        z = results.get("zernio", {}).get("data", {})
                        for p in z.get("platforms", []):
                            if p.get("platform") == "tiktok":
                                tiktok_status = "✅ Published" if p.get("status") == "published" else f"⏳ {p.get('status')}"
                            elif p.get("platform") == "instagram":
                                ig_status = "✅ Published" if p.get("status") == "published" else f"⏳ {p.get('status')}"
                        break
        except Exception:
            pass

    lines = [
        "🌿 <b>LAPORAN AUTOPILOT: DITA GENTLE WELLNESS</b>",
        "━━━━━━━━━━━━━━━━━━━━━",
        f"📅 <b>Waktu:</b> {now_wib}",
        f"🎬 <b>Episode:</b> Day {pad_day}/180",
        f"📌 <b>Topik:</b> {topic}",
        f"🏛️ <b>Pilar:</b> {pillar}",
        "",
        "📊 <b>Status Multi-Platform:</b>",
    ]

    if yt_url:
        lines.append(f"  • YouTube Shorts: <a href='{yt_url}'>▶️ Tonton Shorts</a>")
    else:
        lines.append("  • YouTube Shorts: ❌ Gagal / Tidak tersedia")

    lines.append(f"  • TikTok (@ditawellness): {tiktok_status}")
    lines.append(f"  • Instagram Reels (@ditawellness): {ig_status}")
    lines.append("")
    lines.append("✨ <i>Pipeline on-the-fly selesai dengan sukses tanpa cela visual & audio.</i>")
    lines.append("━━━━━━━━━━━━━━━━━━━━━")
    lines.append("🤖 <i>Herman — Chief AI Orchestrator</i>")

    send_telegram("\n".join(lines))

def report_failure(day_num: int, error_msg: str):
    now_wib = datetime.now(WIB).strftime("%A, %d %b %Y %H:%M WIB")
    pad_day = f"{day_num:03d}" if day_num else "UNKNOWN"
    
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    run_url = f"https://github.com/ditaqsyahm-source/wellness/actions/runs/{run_id}" if run_id else ""

    lines = [
        "🚨 <b>ALERT PIPELINE GAGAL: DITA GENTLE WELLNESS</b>",
        "━━━━━━━━━━━━━━━━━━━━━",
        f"📅 <b>Waktu:</b> {now_wib}",
        f"🎬 <b>Target Episode:</b> Day {pad_day}/180",
        "",
        "❌ <b>Detail Kerusakan / Exception:</b>",
        f"<code>{error_msg[:1000]}</code>",
        "",
    ]

    if run_url:
        lines.append(f"🔍 <b>GitHub Action Log:</b> <a href='{run_url}'>Lihat Log Eksekusi</a>")
        lines.append("")

    lines.append("⚠️ <i>Sistem membutuhkan investigasi arsitektur segera.</i>")
    lines.append("━━━━━━━━━━━━━━━━━━━━━")
    lines.append("🤖 <i>Herman — Chief AI Orchestrator</i>")

    send_telegram("\n".join(lines))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--failure":
        day = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 0
        err = sys.argv[3] if len(sys.argv) > 3 else "Unknown pipeline error"
        report_failure(day, err)
    else:
        day = 1
        for i, a in enumerate(sys.argv):
            if a == "--day" and i + 1 < len(sys.argv):
                day = int(sys.argv[i + 1])
            elif a.isdigit() and i > 0:
                day = int(a)
        report_success(day)
