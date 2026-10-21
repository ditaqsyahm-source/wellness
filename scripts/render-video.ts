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

  // Dynamic sequence configuration based on packet anatomy
  let scenes = [
    { scene_id: "SCENE_01_BEDROOM", timeStart: 0, timeEnd: 5.0, videoSrc: "wellness/scene1_bedroom.mp4" },
    { scene_id: "SCENE_02_HYPERFRAMES_SCN", timeStart: 5.0, timeEnd: 21.0, videoSrc: "wellness/hyperframes_circadian.mp4" },
    { scene_id: "SCENE_03_SUNLIGHT", timeStart: 21.0, timeEnd: 35.0, videoSrc: "wellness/scene3_sunlight.mp4" },
    { scene_id: "SCENE_04_TEA", timeStart: 35.0, timeEnd: 44.0, videoSrc: "wellness/scene4_tea.mp4" },
    { scene_id: "SCENE_05_NATURE", timeStart: 44.0, timeEnd: 55.5, videoSrc: "wellness/scene5_nature.mp4" },
  ];

  const anatomy = packet.script_architecture_breakdown?.anatomy;
  if (Array.isArray(anatomy) && anatomy.length > 0) {
    const brollPool = [
      "wellness/scene1_bedroom.mp4",
      "wellness/scene3_sunlight.mp4",
      "wellness/hyperframes_circadian.mp4",
      "wellness/scene4_tea.mp4",
      "wellness/scene5_nature.mp4"
    ];
    let curTime = 0;
    scenes = anatomy.map((seg: any, idx: number) => {
      const dur = seg.duration_seconds || 10;
      const start = curTime;
      const end = curTime + dur;
      curTime = end;
      return {
        scene_id: seg.segment_id || `SCENE_${idx + 1}`,
        timeStart: start,
        timeEnd: end,
        videoSrc: brollPool[idx % brollPool.length],
      };
    });
  }

  const inputProps = {
    channelName: "Dita Gentle Wellness",
    channelHandle: "@ditawellness",
    title: packet.social_fleet_distribution_metadata?.title || "Ritme Sirkadian: Jam Master Tubuh",
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
