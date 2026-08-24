#!/usr/bin/env python3
"""Rebuild body/engine.py from parts if needed."""
from pathlib import Path
root = Path(__file__).resolve().parent
p1, p2, out = root/"engine_p1.txt", root/"engine_p2.txt", root/"engine.py"
if out.exists():
    print("engine.py already present")
elif p1.exists() and p2.exists():
    out.write_text(p1.read_text()+p2.read_text())
    print("stitched", out)
else:
    print("missing parts")
