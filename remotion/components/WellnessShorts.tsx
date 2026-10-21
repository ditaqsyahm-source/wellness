import React from "react";
import {
  AbsoluteFill,
  Audio,
  Video,
  Sequence,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
} from "remotion";

export interface WellnessSceneItem {
  scene_id?: string;
  timeStart: number;
  timeEnd: number;
  videoSrc: string;
}

export interface WellnessShortsProps {
  channelName?: string;
  channelHandle?: string;
  title?: string;
  hookHeadline?: string;
  hookCategory?: string;
  script: string;
  audioFile?: string;
  scenes?: WellnessSceneItem[];
}

function chunkWords(text: string, maxWords = 4): string[] {
  const words = text.split(/\s+/).filter(Boolean);
  const out: string[] = [];
  for (let i = 0; i < words.length; i += maxWords) {
    out.push(words.slice(i, i + maxWords).join(" "));
  }
  return out;
}

export const WellnessShorts: React.FC<WellnessShortsProps> = ({
  channelName = "Dita Gentle Wellness",
  channelHandle = "@ditawellness",
  title = "Ritme Sirkadian: Jam Master Tubuh",
  hookHeadline,
  hookCategory = "⚠️ PROTOKOL BIOLOGIS",
  script,
  audioFile = "voiceover_day_001.mp3",
  scenes = [],
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  // Progress Bar
  const totalProgress = frame / durationInFrames;

  // Subtitle synchronization
  const lines = chunkWords(script);
  const lineDuration = Math.max(1, Math.floor(durationInFrames / Math.max(lines.length, 1)));
  const lineIndex = Math.min(lines.length - 1, Math.floor(frame / lineDuration));
  const currentLine = lines[lineIndex] || "";
  const progressInLine = (frame % lineDuration) / lineDuration;

  // Kinetic subtitle spring animation
  const textScale = spring({
    frame: frame % lineDuration,
    fps,
    config: { damping: 14, stiffness: 130 },
  });

  const textOpacity = interpolate(progressInLine, [0, 0.1, 0.9, 1], [0.4, 1, 1, 0.5], {
    extrapolateRight: "clamp",
    extrapolateLeft: "clamp",
  });

  // Background subtle breathing zoom
  const bgScale = interpolate(frame, [0, durationInFrames], [1, 1.05], {
    extrapolateRight: "clamp",
  });

  // Hook Banner Opacity (first 4.5 seconds)
  const hookBannerOpacity = interpolate(frame, [0, fps * 3.8, fps * 4.8], [1, 1, 0], {
    extrapolateRight: "clamp",
  });

  // Outro Card (final 3.5 seconds)
  const outroStartFrame = durationInFrames - Math.round(fps * 3.5);
  const outroOpacity = interpolate(frame, [outroStartFrame, outroStartFrame + 15], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#08100b",
        color: "#ffffff",
        fontFamily: "'Segoe UI', Roboto, 'Georgia', serif",
        overflow: "hidden",
      }}
    >
      {/* 1. Voiceover Audio */}
      <Audio src={staticFile(audioFile)} />

      {/* 2. Video Track: B-Roll + HyperFrames Sequences */}
      <AbsoluteFill style={{ transform: `scale(${bgScale})` }}>
        {scenes && scenes.length > 0 ? (
          scenes.map((sc, idx) => {
            const startFrame = Math.round((sc.timeStart || 0) * fps);
            const endFrame = Math.round((sc.timeEnd || durationInFrames / fps) * fps);
            const duration = Math.max(1, endFrame - startFrame);

            return (
              <Sequence
                key={`${sc.scene_id || idx}-${startFrame}`}
                from={startFrame}
                durationInFrames={duration}
              >
                <Video
                  src={staticFile(sc.videoSrc)}
                  muted
                  style={{
                    width: "100%",
                    height: "100%",
                    objectFit: "cover",
                  }}
                />
              </Sequence>
            );
          })
        ) : (
          <div
            style={{
              width: "100%",
              height: "100%",
              background: "linear-gradient(180deg, #122117 0%, #08100b 100%)",
            }}
          />
        )}
      </AbsoluteFill>

      {/* 3. Aesthetic Dark Vignette Overlay for Crisp Readability */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(8, 16, 11, 0.72) 0%, rgba(8, 16, 11, 0.15) 30%, rgba(8, 16, 11, 0.25) 65%, rgba(8, 16, 11, 0.88) 100%)",
          pointerEvents: "none",
        }}
      />

      {/* 4. Top Header Branding Badge (Always Visible & Elegant) */}
      <div
        style={{
          position: "absolute",
          top: 55,
          left: 0,
          right: 0,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          zIndex: 40,
        }}
      >
        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 10,
            background: "rgba(14, 28, 19, 0.85)",
            border: "1px solid rgba(212, 175, 55, 0.45)",
            borderRadius: 9999,
            padding: "8px 22px",
            boxShadow: "0 8px 32px rgba(0, 0, 0, 0.45)",
            backdropFilter: "blur(10px)",
          }}
        >
          <div
            style={{
              width: 8,
              height: 8,
              borderRadius: "50%",
              backgroundColor: "#d4af37",
              boxShadow: "0 0 10px #d4af37",
            }}
          />
          <span
            style={{
              fontSize: 13,
              fontWeight: 700,
              letterSpacing: 2,
              textTransform: "uppercase",
              color: "#e5ecd6",
            }}
          >
            {channelName} • BIOHACKING
          </span>
        </div>
      </div>

      {/* 5. Opening Shock Hook Pill (Detik 0 - 4.5) */}
      {hookBannerOpacity > 0 && (
        <div
          style={{
            position: "absolute",
            top: 130,
            left: 40,
            right: 40,
            opacity: hookBannerOpacity,
            zIndex: 35,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            textAlign: "center",
          }}
        >
          <div
            style={{
              background: "rgba(35, 18, 18, 0.92)",
              border: "1.5px solid rgba(224, 108, 117, 0.6)",
              borderRadius: 16,
              padding: "16px 24px",
              boxShadow: "0 12px 35px rgba(0,0,0,0.6)",
            }}
          >
            <span
              style={{
                fontSize: 12,
                fontWeight: 800,
                letterSpacing: 2.5,
                textTransform: "uppercase",
                color: "#f87171",
                display: "block",
                marginBottom: 6,
              }}
            >
              {hookCategory.toUpperCase()}
            </span>
            <h2
              style={{
                fontSize: 24,
                fontWeight: 800,
                lineHeight: 1.25,
                color: "#ffffff",
                margin: 0,
                textTransform: "uppercase",
              }}
            >
              {hookHeadline || title}
            </h2>
          </div>
        </div>
      )}

      {/* 6. Kinetic Subtitles (Sacred Subtitle Safe Zone: bottom: 200px) */}
      <div
        style={{
          position: "absolute",
          bottom: 210,
          left: 40,
          right: 40,
          textAlign: "center",
          zIndex: 50,
          display: "flex",
          justifyContent: "center",
        }}
      >
        <div
          style={{
            transform: `scale(${textScale})`,
            opacity: textOpacity,
            background: "rgba(10, 20, 14, 0.75)",
            border: "1px solid rgba(164, 190, 172, 0.3)",
            borderRadius: 14,
            padding: "14px 24px",
            boxShadow: "0 8px 30px rgba(0, 0, 0, 0.6)",
            backdropFilter: "blur(8px)",
            maxWidth: 620,
          }}
        >
          <span
            style={{
              fontSize: 28,
              fontWeight: 800,
              lineHeight: 1.35,
              color: "#ffffff",
              textShadow: "0 2px 10px rgba(0, 0, 0, 0.8)",
              letterSpacing: 0.5,
            }}
          >
            {currentLine.split(" ").map((word, wIdx) => {
              const isHighlight =
                word.toLowerCase().includes("hp") ||
                word.toLowerCase().includes("mata") ||
                word.toLowerCase().includes("foton") ||
                word.toLowerCase().includes("sirkadian") ||
                word.toLowerCase().includes("kortisol") ||
                word.toLowerCase().includes("melatonin") ||
                word.toLowerCase().includes("hangat") ||
                word.toLowerCase().includes("tidur");

              return (
                <span
                  key={wIdx}
                  style={{
                    color: isHighlight ? "#d4af37" : "#f1f5f9",
                    textShadow: isHighlight
                      ? "0 0 16px rgba(212, 175, 55, 0.6)"
                      : "none",
                  }}
                >
                  {word}{" "}
                </span>
              );
            })}
          </span>
        </div>
      </div>

      {/* 7. Bottom Elegant Progress Bar */}
      <div
        style={{
          position: "absolute",
          bottom: 0,
          left: 0,
          width: "100%",
          height: 6,
          backgroundColor: "rgba(255, 255, 255, 0.12)",
          zIndex: 60,
        }}
      >
        <div
          style={{
            height: "100%",
            width: `${totalProgress * 100}%`,
            background: "linear-gradient(90deg, #4a6b53 0%, #d4af37 100%)",
            boxShadow: "0 0 12px rgba(212, 175, 55, 0.8)",
          }}
        />
      </div>

      {/* 8. Outro Branding Card (Final 3.5s) */}
      {outroOpacity > 0 && (
        <AbsoluteFill
          style={{
            opacity: outroOpacity,
            backgroundColor: "rgba(8, 16, 11, 0.92)",
            zIndex: 55,
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
            textAlign: "center",
            padding: 40,
            backdropFilter: "blur(14px)",
          }}
        >
          <div
            style={{
              width: 80,
              height: 80,
              borderRadius: "50%",
              border: "2px solid #d4af37",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: 38,
              marginBottom: 20,
              boxShadow: "0 0 25px rgba(212, 175, 55, 0.4)",
            }}
          >
            🌿
          </div>
          <h2
            style={{
              fontSize: 32,
              fontWeight: 800,
              color: "#ffffff",
              marginBottom: 8,
              letterSpacing: 1,
            }}
          >
            {channelName}
          </h2>
          <p
            style={{
              fontSize: 16,
              color: "#a4beac",
              marginBottom: 24,
            }}
          >
            Harmoni Tubuh & Ketenangan Alami
          </p>
          <div
            style={{
              background: "rgba(212, 175, 55, 0.15)",
              border: "1px solid rgba(212, 175, 55, 0.5)",
              borderRadius: 9999,
              padding: "10px 24px",
              fontSize: 15,
              fontWeight: 700,
              color: "#f5d77f",
            }}
          >
            Simpan & Praktikkan Besok Pagi ✨
          </div>
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};
