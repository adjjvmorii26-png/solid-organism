#!/usr/bin/env python3
"""Particle Weather — named storms from mood/crosstalk/genesis pressure."""
from __future__ import annotations
import time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _shared import rng, clamp
STORMS = ["quiet", "drift", "arc-shower", "birth-squall", "coherence-front", "void-calm"]
def fire(ctx=None):
    ctx = ctx or {}
    temp = float((ctx.get("mood") or {}).get("phase") or 0.5)
    wind = float((ctx.get("crosstalk") or {}).get("coherence") or 0.5)
    pressure = float((ctx.get("recursive") or {}).get("halo") or 0.5)
    birth = bool((ctx.get("birth") or {}).get("event"))
    density = clamp((temp + wind + pressure) / 3 + (0.15 if birth else 0))
    idx = min(len(STORMS) - 1, int(density * len(STORMS)))
    if birth: idx = STORMS.index("birth-squall")
    r = rng("wx")
    return {"module": "weather", "state": "particle-weather-autonomy-active",
        "temperature": round(temp, 3), "wind": round(wind, 3),
        "pressure": round(pressure, 3), "density": round(density, 3),
        "speed": round(0.3 + density * 1.2, 2),
        "direction": r.choice(["N", "NE", "E", "SE", "S", "SW", "W", "NW", "spiral"]),
        "storm": STORMS[idx],
        "visual": ["weather_patterns", "storm_events", "climate_shift"],
        "hooks": ["mood-steering", "lateral-crosstalk", "organ-birth"], "ts": time.time()}
if __name__ == "__main__":
    import json; print(json.dumps(fire(), indent=2))
