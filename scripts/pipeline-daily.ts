import fs from "fs";
import path from "path";
import { execSync } from "child_process";
import dotenv from "dotenv";

dotenv.config();

const ROOT_DIR = process.cwd();
const CAMPAIGN_STATE_PATH = path.join(ROOT_DIR, "state", "campaign_state.json");
const PUBLISHED_PATH = path.join(ROOT_DIR, "state", "published.json");

function pad3(num: number): string {
  return String(num).padStart(3, "0");
}

function runCmd(cmd: string) {
  console.log(`\n>>> [EXEC] ${cmd}`);
  execSync(cmd, { stdio: "inherit", cwd: ROOT_DIR });
}

async function main() {
  console.log("============================================================");
  console.log("  DITA GENTLE WELLNESS (@ditawellness) AUTONOMOUS PIPELINE  ");
  console.log("============================================================");

  // 1. Resolve Target Day
  let dayNum: number = 2; // Default to next day
  const args = process.argv.slice(2);
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--day" && args[i + 1]) {
      dayNum = Number(args[i + 1]);
    }
  }

  if (fs.existsSync(CAMPAIGN_STATE_PATH) && !args.includes("--day")) {
    try {
      const state = JSON.parse(fs.readFileSync(CAMPAIGN_STATE_PATH, "utf-8"));
      dayNum = state.next_day || (state.active_day ? state.active_day + 1 : 2);
    } catch (e) {
      console.warn("Could not read campaign state, defaulting to day", dayNum);
    }
  }

  console.log(`Targeting Day: ${dayNum} (${pad3(dayNum)}/180)`);

  const packetFile = path.join(ROOT_DIR, "curriculum", `content_packet_day_${pad3(dayNum)}.json`);
  if (!fs.existsSync(packetFile)) {
    console.error(`[Error] Packet file not found: ${packetFile}`);
    process.exit(1);
  }

  const packet = JSON.parse(fs.readFileSync(packetFile, "utf-8"));
  console.log(`Episode Title: ${packet.metadata?.cycle_theme} - ${packet.social_fleet_distribution_metadata?.title}`);

  // 2. Ensure Voiceover Audio Exists
  const audioFile = path.join(ROOT_DIR, "public", `voiceover_day_${pad3(dayNum)}.mp3`);
  if (!fs.existsSync(audioFile) || fs.statSync(audioFile).size < 10000) {
    console.log(`[Audio] Voiceover not found for Day ${dayNum}, synthesizing via Edge TTS...`);
    runCmd(`python3 scripts/batch_generate_voiceovers.py`);
  }

  // 3. Render Remotion Video Shorts
  const masterMp4 = path.join(ROOT_DIR, "output", `dita_wellness_day_${pad3(dayNum)}_master.mp4`);
  const compressedMp4 = path.join(ROOT_DIR, "output", `dita_wellness_day_${pad3(dayNum)}_compressed.mp4`);
  fs.mkdirSync(path.join(ROOT_DIR, "output"), { recursive: true });

  console.log(`[Render] Compiling Remotion + HyperFrames for Day ${dayNum}...`);
  runCmd(`npx tsx scripts/render-video.ts --day ${dayNum} --out "${masterMp4}"`);

  // 4. Pre-Upload Hardware / Software Compression (< 3.8 MB for Zernio limit)
  console.log(`[Compression] Compressing to < 3.8 MB...`);
  runCmd(
    `ffmpeg -y -i "${masterMp4}" -vf "scale=720:1280" -c:v libx264 -crf 30 -preset fast -c:a aac -b:a 64k -ar 44100 "${compressedMp4}"`
  );

  const compStat = fs.statSync(compressedMp4);
  console.log(`[Compression] Compressed MP4 Size: ${(compStat.size / (1024 * 1024)).toFixed(2)} MB`);

  // 5. Multi-Platform Publication (YouTube Shorts, TikTok, Instagram)
  console.log(`[Publish] Dispatching to YouTube Shorts, TikTok & Instagram Reels...`);
  runCmd(`python3 scripts/publish_video.py`);

  // 6. Advance Campaign State
  if (fs.existsSync(CAMPAIGN_STATE_PATH)) {
    try {
      const state = JSON.parse(fs.readFileSync(CAMPAIGN_STATE_PATH, "utf-8"));
      state.active_day = dayNum;
      state.next_day = dayNum + 1;
      state.total_published = (state.total_published || 1) + 1;
      state.last_updated = new Date().toISOString();
      state.pipeline_status[`day_${pad3(dayNum)}`] = "PUBLISHED";
      fs.writeFileSync(CAMPAIGN_STATE_PATH, JSON.stringify(state, null, 2), "utf-8");
      console.log(`[State] Advanced active_day to ${dayNum}, next_day to ${dayNum + 1}`);
    } catch (e) {
      console.warn("Could not advance campaign state:", e);
    }
  }

  console.log("\n============================================================");
  console.log(`  DAY ${pad3(dayNum)} PIPELINE COMPLETED SUCCESSFULLY!`);
  console.log("============================================================");
}

main().catch((err) => {
  console.error("Pipeline failure:", err);
  process.exit(1);
});
