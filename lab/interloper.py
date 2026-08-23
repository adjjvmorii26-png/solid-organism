#!/usr/bin/env python3
"""Interloper — guest agent for one pulse only."""
import sys, time, random
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save, run_pulse
NAMES = ["Mote", "Cinder", "Quill", "Nix", "Lumen-stray", "Ferry"]
name = random.Random(int(time.time()) // 60).choice(NAMES)
st = ensure_scores(load())
guest = {"id": f"interloper-{name.lower()}", "name": name, "role": "guest", "ttl": 1}
st["agents"] = list(st.get("agents") or []) + [guest]
st["bus"] = (st.get("bus") or [])
st["bus"].insert(0, {"from": name, "note": f"{name} arrives for one pulse only", "ts": time.time()})
try: st = run_pulse(st)
except Exception: pass
st["agents"] = [a for a in (st.get("agents") or []) if a.get("id") != guest["id"]]
st["bus"].insert(0, {"from": name, "note": f"{name} departs — scar left on the bus", "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(f"interloper · {name} arrived and left")
