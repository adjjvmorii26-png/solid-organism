#!/usr/bin/env python3
"""Seed crystal — lock one organ score as immutable reference."""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

st = ensure_scores(load())
organs = st.get("organs") or []
pick = max((o for o in organs if not o.get("crystal")), key=lambda o: float(o.get("score", 0)), default=None)
if not pick:
    print("crystal · all facets locked"); raise SystemExit(0)
pick["crystal"] = True
pick["crystal_score"] = float(pick["score"])
note = f"crystal · {pick['id']} locked at {pick['crystal_score']:.2f}"
st["bus"] = (st.get("bus") or [])
st["bus"].insert(0, {"from": "crystal", "note": note, "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(note)
