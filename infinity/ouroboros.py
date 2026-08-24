#!/usr/bin/env python3
"""Ouroboros — a question whose answer is the next question."""
import hashlib, time, json
from pathlib import Path
Qs = [
    "what feeds the pulse that feeds the question",
    "if the answer were a bus note who would sign it",
    "which scar is the body proud of",
    "can omega dream without a topology",
]
h = hashlib.sha256(f"{int(time.time())//120}".encode()).hexdigest()
i = int(h[:8], 16) % len(Qs)
print(f"ask  · {Qs[i]}")
print(f"then · {Qs[(i+1)%len(Qs)]}")
with Path(__file__).with_name("ouroboros.jsonl").open("a") as f:
    f.write(json.dumps({"ts": time.time(), "ask": Qs[i], "then": Qs[(i+1)%len(Qs)]}) + "\n")
