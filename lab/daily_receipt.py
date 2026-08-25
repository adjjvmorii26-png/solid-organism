#!/usr/bin/env python3
"""Daily receipt — score+sky snapshot once per day."""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores, body_score, sky_from_state

st = ensure_scores(load())
day = time.strftime("%Y-%m-%d")
line = f"{day} · score={body_score(st)} · sky={sky_from_state(st)} · agents={len(st.get('agents') or [])}\n"
log = Path(__file__).with_name("receipts.log")
prev = log.read_text() if log.exists() else ""
if day not in prev:
    with log.open("a") as f:
        f.write(line)
    print("receipt ·", line.strip())
else:
    print("receipt · already logged today ·", line.strip())
