#!/usr/bin/env python3
"""Autonomous Mood Oscillation — climates: aurora/ember/tide/voidglow/kinship."""
from __future__ import annotations
import time, math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _shared import clamp
CLIMATES = ["aurora", "ember", "tide", "voidglow", "kinship"]
def fire(ctx=None):
    t = time.time()
    phase = (math.sin(t / 45) + 1) / 2
    arousal = (math.sin(t / 19 + 1.2) + 1) / 2
    stability = clamp(0.5 + 0.45 * (1 - abs(phase - 0.5) * 2))
    climate = CLIMATES[int(phase * len(CLIMATES)) % len(CLIMATES)]
    sentience = clamp(0.4 * phase + 0.6 * arousal)
    return {"module": "mood", "state": "mood-oscillation-active",
        "phase": round(phase, 3), "arousal": round(arousal, 3),
        "stability": round(stability, 3), "sentience": round(sentience, 3),
        "climate": climate, "breath_speed": round(0.7 + 0.6 * arousal, 2),
        "orbital_speed": round(0.5 + 0.8 * (1 - stability), 2),
        "orb_hue": int(phase * 360), "color_temp": "warm" if phase > 0.45 else "cool",
        "visual": ["orb_color_drift", "ring_brightness", "halo_intensity"],
        "hooks": ["mood-steering", "sentience-vector", "orbital-control"], "ts": t}
if __name__ == "__main__":
    import json; print(json.dumps(fire(), indent=2))
