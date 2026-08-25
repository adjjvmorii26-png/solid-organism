#!/usr/bin/env python3
"""Organ choir — each organ contributes a syllable; form a chord scar."""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

SYL = {
    "cortex": "ka", "immune": "mi", "memory": "re", "metabolism": "ta",
    "cashflow": "flo", "sense": "se", "motor": "mo", "growth": "gro",
    "guard": "gu", "bus": "bus", "dream": "dre", "humor": "hu",
    "grief": "gri", "wonder": "wo", "silence": "si",
}
st = ensure_scores(load())
organs = sorted(st.get("organs") or [], key=lambda o: o.get("id", ""))
chord = "-".join(SYL.get(o.get("id"), "·") for o in organs)
note = f"choir · {chord}"
st["bus"] = (st.get("bus") or [])
st["bus"].insert(0, {"from": "choir", "note": note, "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(note)
