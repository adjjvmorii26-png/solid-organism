#!/usr/bin/env python3
"""Echo chamber — last bus note speaks back in reversed tokens."""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

st = ensure_scores(load())
bus = st.get("bus") or []
if not bus:
    print("echo · silent chamber"); raise SystemExit(0)
tokens = (bus[0].get("note") or "…").split()
note = f"echo · «{' '.join(reversed(tokens))[:70]}»"
st["bus"] = list(bus)
st["bus"].insert(0, {"from": "echo", "note": note, "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(note)
