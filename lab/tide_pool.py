#!/usr/bin/env python3
"""Tide pool — all organs share one tidal phase."""
import sys, time, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save, clamp_organ

st = ensure_scores(load())
phase = (math.sin(time.time() / 600) + 1) / 2
for o in st.get("organs") or []:
    if o.get("crystal"):
        continue
    s = float(o.get("score", 0.9))
    o["score"] = clamp_organ(s * 0.85 + (0.82 + 0.14 * phase) * 0.15)
note = f"tide · phase={phase:.2f} · organs drift with the pool"
st["bus"] = (st.get("bus") or [])
st["bus"].insert(0, {"from": "tide", "note": note, "ts": time.time()})
st["bus"] = st["bus"][:40]
save(ensure_scores(st))
print(note)
