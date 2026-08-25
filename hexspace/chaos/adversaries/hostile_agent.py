#!/usr/bin/env python3
"""Hostile agent — soft attack vector (log only)."""
import json, time
from pathlib import Path
MEM = Path(__file__).with_name("adversary_memory.json")
def probe() -> dict:
    p = {"ts": time.time(), "vector": "bus_flood_sim", "blocked": True}
    hist = json.loads(MEM.read_text()) if MEM.exists() else []
    hist.append(p)
    MEM.write_text(json.dumps(hist[-20:], indent=2))
    return p
if __name__ == "__main__":
    print("hostile ·", probe())
