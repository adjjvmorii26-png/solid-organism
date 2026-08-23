#!/usr/bin/env python3
"""Cordyceps — a random agent temporarily steers a foreign organ."""
import random, time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

st = ensure_scores(load())
agents = st.get("agents") or []
organs = st.get("organs") or []
if not agents or not organs:
    print("cordyceps · empty"); raise SystemExit(0)
rng = random.Random(int(time.time()) // 45)
agent = rng.choice(agents)
organ = rng.choice(organs)
organ["score"] = min(0.99, float(organ.get("score", 0.8)) + 0.015)
note = f"cordyceps · {agent.get('name') or agent.get('id')} steers {organ.get('id')}"
st["bus"] = (st.get("bus") or [])
st["bus"].insert(0, {"from": "cordyceps", "note": note, "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(note)
