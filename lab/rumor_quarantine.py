#!/usr/bin/env python3
"""Rumor quarantine — isolate rumor/suture scars to side channel."""
import sys, time, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, save

st = ensure_scores(load())
bus = list(st.get("bus") or [])
keep, iso = [], []
for m in bus:
    fr = (m.get("from") or "").lower()
    if fr in ("rumor", "suture") or "rumor" in (m.get("note") or "").lower():
        iso.append(m)
    else:
        keep.append(m)
st["bus"] = keep[:40]
with Path(__file__).with_name("quarantine.jsonl").open("a") as f:
    for m in iso:
        f.write(json.dumps({"ts": time.time(), **m}) + "\n")
note = f"quarantine · isolated {len(iso)} · bus now {len(keep)}"
st["bus"].insert(0, {"from": "quarantine", "note": note, "ts": time.time()})
st["bus"] = st["bus"][:40]
save(st)
print(note)
