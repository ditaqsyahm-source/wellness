import React from "react";
import { Composition } from "remotion";
import { WellnessShorts, type WellnessShortsProps } from "./components/WellnessShorts";

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="WellnessShorts"
      component={WellnessShorts as React.ComponentType}
      durationInFrames={1333} // ~55.5s @24fps default
      fps={24}
      width={720}
      height={1280}
      defaultProps={{
        channelName: "Dita Gentle Wellness",
        channelHandle: "@ditawellness",
        title: "Ritme Sirkadian: Jam Master Tubuh",
        script: "Hentikan kebiasaan langsung membuka layar HP di menit-menit pertama kamu membuka mata! Cahaya redup layar gawai membingungkan sensor retina matamu. Akibatnya, hormon kortisol alami gagal memuncak dengan benar, memicu rasa cemas, dan menahan tubuhmu dalam kelelahan.",
        audioFile: "voiceover_day_001.mp3",
      } as WellnessShortsProps}
    />
  );
};
