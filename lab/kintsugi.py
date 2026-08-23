#!/usr/bin/env python3
"""Kintsugi — mend the weakest organ; leave a golden scar on the bus."""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

st = ensure_scores(load())
organs = st.get("organs") or []
if not organs:
    print("kintsugi · no organs"); raise SystemExit(0)
weak = min(organs, key=lambda o: float(o.get("score", 0)))
before = float(weak["score"])
weak["score"] = min(0.99, before + 0.04)
scar = f"kintsugi · {weak.get('id')} {before:.2f}→{weak['score']:.2f} (gold join)"
st["bus"] = (st.get("bus") or [])
st["bus"].insert(0, {"from": "kintsugi", "note": scar, "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(scar)
