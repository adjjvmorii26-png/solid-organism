#!/usr/bin/env python3
"""Tide clock — organ phases on one wave."""
import math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores
st = ensure_scores(load())
t = __import__("time").time()
print("tide · phase of each organ")
for i, o in enumerate(st.get("organs") or []):
    s = float(o.get("score", 0.5))
    phase = (math.sin(t * 0.01 + i * 0.7 + s * 6.28) + 1) / 2
    bar = "█" * int(phase * 12) + "·" * (12 - int(phase * 12))
    print(f"  {str(o.get('id', i)):12} {bar} {phase:.2f}")
