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

    print(f"Synthesizing Day {day_num} ({len(text.split())} words)...")
    comm = edge_tts.Communicate(text, VOICE, rate="+0%", pitch="+0Hz")
    
    for attempt in range(1, 4):
        try:
            await comm.save(out_path1)
            if os.path.exists(out_path1) and os.path.getsize(out_path1) > 5000:
                import shutil
                shutil.copyfile(out_path1, out_path2)
                print(f"✅ Day {day_num} saved -> {file_name} ({os.path.getsize(out_path1)} bytes)")
                return
        except Exception as e:
            print(f"⚠️ Day {day_num} attempt {attempt} failed: {e}")
            await asyncio.sleep(2 * attempt)

    print(f"❌ Day {day_num} failed after 3 attempts.")

async def main():
    print("=== BATCH SYNTHESIZING VOICEOVERS DAY 002 - DAY 030 ===")
    for day_num in range(2, 31):
        packet_file = os.path.join(CURRICULUM_PATH, f"content_packet_day_{str(day_num).zfill(3)}.json")
        if not os.path.exists(packet_file):
            print(f"Packet file not found: {packet_file}")
            continue
        with open(packet_file, "r", encoding="utf-8") as f:
            packet = json.load(f)
        text = packet.get("verbatim_script_master", {}).get("full_spoken_text_id", "")
        if not text:
            print(f"No text in packet Day {day_num}")
            continue

        await synthesize_one(day_num, text)
        await asyncio.sleep(0.4) # respectful throttling

    print("\n[SUCCESS] Batch Voiceover Synthesis Completed!")

if __name__ == "__main__":
    asyncio.run(main())
