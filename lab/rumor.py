#!/usr/bin/env python3
"""Rumor mill — note mutates across agent hops."""
import sys, time, random
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save
REPL = [("score", "weather"), ("pulse", "heartbeat"), ("organ", "creature"), ("bus", "whisper-net"), ("healthier", "stranger")]
st = ensure_scores(load())
bus = st.get("bus") or []
msg = (bus[0].get("note") if bus else "leave healthier") or "leave healthier"
agents = [a.get("name") or a.get("id") for a in (st.get("agents") or [])] or ["Anon"]
rng = random.Random(int(time.time()) // 30)
path = []
for _ in range(min(3, max(1, len(agents)))):
    who = rng.choice(agents)
    old, new = rng.choice(REPL)
    msg = msg.replace(old, new)
    path.append(str(who))
note = f"rumor · {' → '.join(path)} · {msg[:80]}"
st["bus"] = list(bus)
st["bus"].insert(0, {"from": "rumor", "note": note, "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(note)
