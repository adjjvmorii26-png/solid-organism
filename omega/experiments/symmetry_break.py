#!/usr/bin/env python3
"""Symmetry break — force topology away from last shape."""
import json, time, random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lattice.topology_engine import SHAPES
last = Path(__file__).with_name("last_shape.json")
prev = "euclid"
if last.exists():
    try: prev = json.loads(last.read_text()).get("shape", prev)
    except Exception: pass
cands = [s for s in SHAPES if s != prev] or list(SHAPES)
shape = random.Random(int(time.time())).choice(cands)
last.write_text(json.dumps({"ts": time.time(), "shape": shape, "broke_from": prev}, indent=2))
print(f"symmetry · broke {prev} → {shape}")
