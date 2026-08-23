#!/usr/bin/env python3
"""Echolalia — a phrase echoes through the bus until the words drift."""
import json, time
from pathlib import Path

SEED = "leave the body healthier than you found it"
MUTATIONS = {
    "leave": ["keep", "gift", "return"],
    "body": ["mesh", "organ", "lattice"],
    "healthier": ["stranger", "quieter", "brighter"],
    "found": ["met", "named", "woke"],
    "it": ["this", "us", "the score"],
}

def echo(n=5, seed=SEED):
    words = seed.split()
    lines = [seed]
    for i in range(n):
        idx = i % len(words)
        w = words[idx]
        opts = MUTATIONS.get(w.lower(), [w])
        words[idx] = opts[i % len(opts)]
        lines.append(" ".join(words))
    return lines

if __name__ == "__main__":
    lines = echo()
    log = Path(__file__).with_name("echolalia.jsonl")
    with log.open("a") as f:
        f.write(json.dumps({"ts": time.time(), "lines": lines}) + "\n")
    for i, L in enumerate(lines):
        print(f"echo[{i}] {L}")
