#!/usr/bin/env python3
"""Mycelium — grow hidden edges between organs; strength decays daily."""
import sys, time, random
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

st = ensure_scores(load())
organs = st.get("organs") or []
if len(organs) < 2:
    print("mycelium · need 2+ organs"); raise SystemExit(0)
ids = [o["id"] for o in organs]
rng = random.Random(int(time.time()) // 120)
a, b = rng.sample(ids, 2)
now = time.time()
links = [L for L in st.get("mycelium") or [] if now - L.get("born", 0) < 86400]
links.append({"a": a, "b": b, "strength": round(0.4 + rng.random() * 0.5, 2), "born": now})
st["mycelium"] = links[-12:]
for o in organs:
    if o["id"] in (a, b):
        o["score"] = min(0.99, float(o["score"]) + 0.008)
note = f"mycelium · {a}⟷{b} ×{links[-1]['strength']} · web={len(links)}"
st["bus"] = (st.get("bus") or [])
st["bus"].insert(0, {"from": "mycelium", "note": note, "ts": now})
st["bus"] = st["bus"][:40]
save(ensure_scores(st))
print(note)
