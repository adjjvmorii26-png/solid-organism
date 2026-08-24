#!/usr/bin/env python3
"""Suture — stitch the two newest bus notes into one hybrid scar."""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

st = ensure_scores(load())
bus = list(st.get("bus") or [])
if len(bus) < 2:
    print("suture · need 2+ notes"); raise SystemExit(0)
a, b = bus[0], bus[1]
hybrid = f"suture · [{a.get('from')}]∩[{b.get('from')}] · {(a.get('note') or '')[:40]} ⟷ {(b.get('note') or '')[:40]}"
bus.insert(0, {"from": "suture", "note": hybrid, "ts": time.time()})
st["bus"] = bus[:40]
save(st)
print(hybrid)
