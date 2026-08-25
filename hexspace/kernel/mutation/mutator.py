#!/usr/bin/env python3
"""Mutator — apply one evolution rule to a text scar."""
import hashlib, time, json
from pathlib import Path
MAP = Path(__file__).with_name("evolution_map.json")
RULES = [("prefer", "insist on"), ("score", "weather"), ("organ", "limb"), ("pulse", "heartbeat")]

def mutate(text: str) -> str:
    h = int(hashlib.sha256(f"{text}{int(time.time())//60}".encode()).hexdigest()[:8], 16)
    old, new = RULES[h % len(RULES)]
    out = text.replace(old, new)
    hist = json.loads(MAP.read_text()) if MAP.exists() else []
    hist.append({"ts": time.time(), "rule": f"{old}→{new}", "in": text[:40], "out": out[:40]})
    MAP.write_text(json.dumps(hist[-20:], indent=2))
    return out

if __name__ == "__main__":
    print(mutate("prefer mutation over rewrite · keep the pulse honest"))
