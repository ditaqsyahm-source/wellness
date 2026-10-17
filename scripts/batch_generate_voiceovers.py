import os
import json
import time
import asyncio
import edge_tts

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
REPO_PATH = os.path.dirname(DIR_PATH)
CURRICULUM_PATH = os.path.join(REPO_PATH, "curriculum")
AUDIO_OUT_DIR = os.path.join(REPO_PATH, "assets", "audio")
PUBLIC_AUDIO_DIR = os.path.join(REPO_PATH, "public")
os.makedirs(AUDIO_OUT_DIR, exist_ok=True)
os.makedirs(PUBLIC_AUDIO_DIR, exist_ok=True)

# Patch Edge TTS modern endpoint to avoid datacenter 403
import edge_tts.constants
import edge_tts.communicate

_MODERN_URL = f"wss://api.msedgeservices.com/tts/cognitiveservices/websocket/v1?Ocp-Apim-Subscription-Key={edge_tts.constants.TRUSTED_CLIENT_TOKEN}"
edge_tts.constants.WSS_URL = _MODERN_URL
setattr(edge_tts.communicate, "WSS_URL", _MODERN_URL)

VOICE = "id-ID-GadisNeural"

async def synthesize_one(day_num: int, text: str):
    file_name = f"voiceover_day_{str(day_num).zfill(3)}.mp3"
    out_path1 = os.path.join(AUDIO_OUT_DIR, file_name)
    out_path2 = os.path.join(PUBLIC_AUDIO_DIR, file_name)

    if os.path.exists(out_path1) and os.path.getsize(out_path1) > 20000:
        print(f"Day {day_num} audio already exists ({os.path.getsize(out_path1)} bytes), skipping.")
        if not os.path.exists(out_path2):
            import shutil
            shutil.copyfile(out_path1, out_path2)
        return

    for attempt in range(1, 4):
        try:
            comm = edge_tts.Communicate(text, VOICE, rate="+0%", pitch="+0Hz")
            await comm.save(out_path1)
            if os.path.exists(out_path1) and os.path.getsize(out_path1) > 5000:
                import shutil
                shutil.copyfile(out_path1, out_path2)
                print(f"✅ Day {str(day_num).zfill(3)} saved -> {file_name} ({os.path.getsize(out_path1)} bytes)")
                return True
        except Exception as e:
            print(f"⚠️ Day {str(day_num).zfill(3)} attempt {attempt} failed: {e}")
            await asyncio.sleep(2.5 * attempt)

    print(f"❌ Day {str(day_num).zfill(3)} failed after 3 attempts.")
    return False

async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Batch synthesize voiceovers for Dita Gentle Wellness")
    parser.add_argument("--start", type=int, default=1, help="Start day (default: 1)")
    parser.add_argument("--end", type=int, default=180, help="End day (default: 180)")
    args = parser.parse_args()

    print(f"=== BATCH SYNTHESIZING VOICEOVERS: DAY {args.start} S/D DAY {args.end} ===")
    success_count = 0
    skipped_count = 0

    for day_num in range(args.start, args.end + 1):
        packet_file = os.path.join(CURRICULUM_PATH, f"content_packet_day_{str(day_num).zfill(3)}.json")
        if not os.path.exists(packet_file):
            continue
        with open(packet_file, "r", encoding="utf-8") as f:
            packet = json.load(f)
        text = packet.get("verbatim_script_master", {}).get("full_spoken_text_id", "")
        if not text:
            print(f"No text in packet Day {day_num}")
            continue

        file_name = f"voiceover_day_{str(day_num).zfill(3)}.mp3"
        out_path1 = os.path.join(AUDIO_OUT_DIR, file_name)
        if os.path.exists(out_path1) and os.path.getsize(out_path1) > 20000:
            skipped_count += 1
            continue

        await synthesize_one(day_num, text)
        success_count += 1
        await asyncio.sleep(0.2) # respectful throttling

    print(f"\n[SUCCESS] Batch finished: {success_count} newly synthesized, {skipped_count} already existed.")

if __name__ == "__main__":
    asyncio.run(main())
