import fs from "fs";
import path from "path";
import { bundle } from "@remotion/bundler";
import { renderMedia, selectComposition } from "@remotion/renderer";

async function main() {
  const args = process.argv.slice(2);
  let dayNum = 1;
  let outputPath = "output/dita_wellness_day_001_master.mp4";

  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--day" && args[i + 1]) dayNum = Number(args[i + 1]);
    if (args[i] === "--out" && args[i + 1]) outputPath = args[i + 1];
  }

  const packetFile = path.resolve(`curriculum/content_packet_day_${String(dayNum).padStart(3, "0")}.json`);
  if (!fs.existsSync(packetFile)) {
    console.error(`Error: Packet file not found: ${packetFile}`);
    process.exit(1);
  }

  const packet = JSON.parse(fs.readFileSync(packetFile, "utf-8"));
  fs.mkdirSync(path.dirname(path.resolve(outputPath)), { recursive: true });

  const script =
    packet.verbatim_script_master?.full_spoken_text_id ||
    packet.script_text ||
    "";

  const dayStr = String(dayNum).padStart(3, "0");
  const dayBrollDir = path.resolve(`public/broll/day_${dayStr}`);

  // Dynamic sequence configuration based on packet anatomy & unique day B-roll
  const anatomy = packet.script_architecture_breakdown?.anatomy;
  const numScenes = Array.isArray(anatomy) && anatomy.length > 0 ? anatomy.length : 5;
  let curTime = 0;
  const scenes = [];

  for (let idx = 0; idx < numScenes; idx++) {
    const scNum = String(idx + 1).padStart(2, "0");
    const dur = anatomy && anatomy[idx]?.duration_seconds ? anatomy[idx].duration_seconds : 10;
    const start = curTime;
    const end = curTime + dur;
    curTime = end;

    // Check if day-specific unique B-roll exists
    const dayClip = path.join(dayBrollDir, `scene_${scNum}.mp4`);
    let videoSrc = `broll/day_${dayStr}/scene_${scNum}.mp4`;
    if (!fs.existsSync(dayClip)) {
      const brollPool = [
        "wellness/scene1_bedroom.mp4",
        "wellness/scene3_sunlight.mp4",
        "wellness/hyperframes_circadian.mp4",
        "wellness/scene4_tea.mp4",
        "wellness/scene5_nature.mp4"
      ];
      videoSrc = brollPool[idx % brollPool.length];
    }

    scenes.push({
      scene_id: anatomy && anatomy[idx]?.segment_id ? anatomy[idx].segment_id : `SCENE_${scNum}`,
      timeStart: start,
      timeEnd: end,
      videoSrc,
    });
  }

  const hookHeadline =
    packet.social_fleet_distribution_metadata?.title?.replace(/#\w+/g, "").trim() ||
    packet.scientific_research_dossier?.core_topic?.split("!")[0]?.trim() ||
    "PERINGATAN SAINS BIOHACKING";

  const hookCategory =
    packet.metadata?.topic_pillar_name ||
    "GENTLE WELLNESS & PENYEJUK HATI";

  const inputProps = {
    channelName: "Dita Gentle Wellness",
    channelHandle: "@ditawellness",
    title: packet.social_fleet_distribution_metadata?.title || "Ritme Sirkadian: Jam Master Tubuh",
    hookHeadline,
    hookCategory,
    script,
    audioFile: `voiceover_day_${String(dayNum).padStart(3, "0")}.mp3`,
    scenes,
  };

  const totalDuration = scenes.length > 0 ? scenes[scenes.length - 1].timeEnd : 55.0;
  const durationInFrames = Math.round(totalDuration * 24) + 12; // safety frames

  console.log(`[Remotion + HyperFrames] Bundling composition entry...`);
  const bundleLocation = await bundle({
    entryPoint: path.resolve("remotion/index.ts"),
    webpackOverride: (config) => config,
  });

  console.log(`[Remotion + HyperFrames] Selecting composition 'WellnessShorts'...`);
  const composition = await selectComposition({
    serveUrl: bundleLocation,
    id: "WellnessShorts",
    inputProps,
  });

  const CHROME =
    process.env.REMOTION_BROWSER_EXECUTABLE ||
    process.env.REMOTION_CHROMIUM_EXECUTABLE ||
    undefined;

  console.log(`[Remotion + HyperFrames] Rendering ${durationInFrames} frames (${totalDuration}s) at 720x1280 @24fps to ${outputPath}...`);

  await renderMedia({
    composition: {
      ...composition,
      durationInFrames,
      fps: 24,
      width: 720,
      height: 1280,
    },
    serveUrl: bundleLocation,
    codec: "h264",
    imageFormat: "jpeg",
    jpegQuality: 70,
    crf: 23,
    outputLocation: path.resolve(outputPath),
    inputProps,
    browserExecutable: CHROME,
    chromiumOptions: (process.platform === "linux"
      ? {
          gl: "swiftshader",
          args: ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"],
        }
      : {
          gl: "angle",
          args: ["--no-sandbox", "--disable-setuid-sandbox", "--use-gl=angle", "--use-angle=d3d11", "--enable-gpu-rasterization"],
        }) as any,
    concurrency: 4,
    onProgress: ({ progress }) => {
      process.stdout.write(`\r[Remotion] Progress: ${(progress * 100).toFixed(0)}%`);
    },
  });

  console.log(`\n[Remotion] Render complete -> ${outputPath}`);
  const stat = fs.statSync(outputPath);
  console.log(`[Remotion] Final MP4 Size: ${(stat.size / (1024 * 1024)).toFixed(2)} MB`);
}

main().catch((err) => {
  console.error("[Remotion] Render failure:", err);
  process.exit(1);
});
