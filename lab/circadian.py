#!/usr/bin/env python3
"""Circadian — metabolism rises by day, memory by night."""
import sys, time, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save, clamp_organ

st = ensure_scores(load())
organs = st.get("organs") or []
hour = time.localtime().tm_hour
phase = (math.sin((hour - 8) / 24 * 2 * math.pi) + 1) / 2
for o in organs:
    oid, s = o.get("id"), float(o.get("score", 0.9))
    if oid == "metabolism":
        o["score"] = clamp_organ(s * 0.7 + (0.85 + 0.12 * phase) * 0.3)
    elif oid == "memory":
        o["score"] = clamp_organ(s * 0.7 + (0.85 + 0.12 * (1 - phase)) * 0.3)
note = f"circadian · hour={hour} day_phase={phase:.2f} metabolism↔memory"
st["bus"] = (st.get("bus") or [])
st["bus"].insert(0, {"from": "circadian", "note": note, "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(note)
