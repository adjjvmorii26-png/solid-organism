#!/usr/bin/env python3
"""Palimpsest — surface text + faded under-layer."""
import json, time
from pathlib import Path
STORE = Path(__file__).with_name("palimpsest.json")
NEW = "the lattice remembers what the score forgets"
def fade(text):
    return "".join(c if i % 2 == 0 else "·" for i, c in enumerate(text))
prev = {}
if STORE.exists():
    try: prev = json.loads(STORE.read_text())
    except Exception: prev = {}
under = fade(prev.get("surface", ""))
STORE.write_text(json.dumps({"ts": time.time(), "surface": NEW, "under": under}, indent=2))
print("surface ·", NEW)
print("under   ·", under or "(first layer)")
