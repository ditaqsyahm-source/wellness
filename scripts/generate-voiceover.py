import os
import sys
import json
import asyncio
import edge_tts
import edge_tts.constants
import edge_tts.communicate
import subprocess

# Fix Microsoft Edge TTS 403 on cloud runners (synthesize via api.msedgeservices.com)
_NEW_WSS = (
    "wss://api.msedgeservices.com/tts/cognitiveservices/websocket/v1"
    f"?Ocp-Apim-Subscription-Key={edge_tts.constants.TRUSTED_CLIENT_TOKEN}"
)
edge_tts.constants.WSS_URL = _NEW_WSS
edge_tts.communicate.WSS_URL = _NEW_WSS

async def synthesize(text, voice, output_path):
    communicate = edge_tts.Communicate(text, voice, rate="+10%")
    await communicate.save(output_path)

def get_audio_duration(file_path):
    try:
        cmd = [
            "ffprobe", "-v", "error", "-show_entries",
            "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file_path
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return float(res.stdout.strip())
    except Exception as e:
        print(f"Warning: ffprobe failed ({e}), using fallback word-count duration")
        # Approximate: 130 words per minute
        words = len(text.split())
        return (words / 130) * 60

def main():
    packet_path = sys.argv[1] if len(sys.argv) > 1 else "curriculum/content_packet_day_001.json"
    output_audio = sys.argv[2] if len(sys.argv) > 2 else "public/voiceover.mp3"

    os.makedirs(os.path.dirname(os.path.abspath(output_audio)), exist_ok=True)

    if not os.path.exists(packet_path):
        print(f"Error: Packet file not found: {packet_path}")
        sys.exit(1)

    with open(packet_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    script_text = (
        data.get("verbatim_script_master", {}).get("full_spoken_text_id")
        or data.get("script_text")
    )
    if not script_text:
        print("Error: No spoken script found in packet")
        sys.exit(1)

    # Dynamic voice resolution based on channel cluster / packet metadata
    voice_pref = data.get("voiceover_persona") or data.get("long_form_youtube", {}).get("voiceover_persona")
    if voice_pref and "Ardi" in str(voice_pref):
        voice = "id-ID-ArdiNeural"
    elif "NASH" in data.get("metadata", {}).get("channel_id", ""):
        voice = "id-ID-ArdiNeural"
    else:
        voice = "id-ID-GadisNeural"
    print(f"[TTS] Synthesizing voiceover with {voice} ({len(script_text.split())} words)...")
    asyncio.run(synthesize(script_text, voice, output_audio))
    print(f"[TTS] Audio saved to {output_audio}")

    duration = get_audio_duration(output_audio)
    duration_frames = int(duration * 24)

    result = {
        "audio_path": output_audio,
        "duration_seconds": round(duration, 2),
        "duration_frames": duration_frames,
        "fps": 24,
        "voice": voice
    }

    # Save audio metadata for Remotion render
    meta_path = "public/audio_meta.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"[TTS] Result: {duration:.2f}s ({duration_frames} frames @30fps)")
    print(json.dumps(result))

if __name__ == "__main__":
    main()
