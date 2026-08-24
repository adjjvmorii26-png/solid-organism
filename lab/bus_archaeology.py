#!/usr/bin/env python3
"""Bus archaeology — reconstruct a short day from bus scars alone."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "body"))
from engine import load, ensure_scores

st = ensure_scores(load())
bus = st.get("bus") or []
tags = {}
for m in bus:
    fr = (m.get("from") or "?").lower()
    tags[fr] = tags.get(fr, 0) + 1
print("archaeology · voices on the bus")
for k, v in sorted(tags.items(), key=lambda x: -x[1])[:12]:
    print(f"  {k:16} ×{v}")
print(f"layers · {len(bus)} notes retained")
