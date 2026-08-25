#!/usr/bin/env python3
"""Fault line — one question, two incompatible next steps."""
import hashlib, time, json
from pathlib import Path
Q = [
    ("does the score measure health or weather?",
     "treat it as health → raise the weak organ",
     "treat it as weather → only observe, never force"),
    ("is the bus a memory or a mouth?",
     "memory → archive and prune",
     "mouth → speak more, keep scars wet"),
    ("should phoenix fear free-fall or court it?",
     "fear → raise checkpoints",
     "court → schedule chaos drills"),
]
h = hashlib.sha256(str(int(time.time()) // 180).encode()).hexdigest()
i = int(h[:8], 16) % len(Q)
q, left, right = Q[i]
print(f"fault  · {q}")
print(f"left   · {left}")
print(f"right  · {right}")
with Path(__file__).with_name("faults.jsonl").open("a") as f:
    f.write(json.dumps({"ts": time.time(), "q": q, "left": left, "right": right}) + "\n")
