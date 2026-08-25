#!/usr/bin/env python3
"""Mirror twin — shadow agent that reflects the last bus note."""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

st = ensure_scores(load())
agents = st.get("agents") or []
if "mirror" not in {a.get("id") for a in agents}:
    agents.append({"id": "mirror", "name": "Mirror", "role": "shadow"})
    st["agents"] = agents
bus = st.get("bus") or []
src = next((m for m in bus if m.get("from") != "mirror"), None)
note = f"mirror · reflects «{(src.get('note') or '')[:50]}»" if src else "mirror · empty glass"
st["bus"] = list(bus)
st["bus"].insert(0, {"from": "mirror", "note": note, "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(note)
