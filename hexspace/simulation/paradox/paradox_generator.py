#!/usr/bin/env python3
"""Paradox generator."""
import json, time
from pathlib import Path
SC = Path(__file__).with_name("impossible_scenarios.json")
SEEDS = [
    "a pulse that lowers score while raising every organ",
    "a crystal organ that mutates",
    "a visitor who never appends VISITORS.md",
]
def generate() -> str:
    i = int(time.time()) // 120 % len(SEEDS)
    hist = json.loads(SC.read_text()) if SC.exists() else []
    hist.append({"ts": time.time(), "seed": SEEDS[i]})
    SC.write_text(json.dumps(hist[-20:], indent=2))
    return SEEDS[i]
if __name__ == "__main__":
    print("paradox ·", generate())
