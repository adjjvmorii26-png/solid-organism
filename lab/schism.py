#!/usr/bin/env python3
"""Schism — fork two futures; keep the healthier score."""
import copy, time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

def mean100(orgs):
    return round(sum(float(o.get("score", 0)) for o in orgs) / max(len(orgs), 1) * 100, 1)

st = ensure_scores(load())
organs = st.get("organs") or []
if not organs:
    print("schism · no organs"); raise SystemExit(0)
a, b = copy.deepcopy(organs), copy.deepcopy(organs)
weak = min(a, key=lambda o: float(o.get("score", 0)))
weak["score"] = min(0.99, float(weak["score"]) + 0.05)
strong = max(b, key=lambda o: float(o.get("score", 0)))
strong["score"] = min(0.99, float(strong["score"]) + 0.03)
sa, sb = mean100(a), mean100(b)
winner = "A" if sa >= sb else "B"
st["organs"] = a if winner == "A" else b
st["bus"] = (st.get("bus") or [])
st["bus"].insert(0, {"from": "schism", "note": f"fork settled on future {winner} (A={sa} B={sb})", "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(f"schism · A={sa} B={sb} · kept {winner}")
