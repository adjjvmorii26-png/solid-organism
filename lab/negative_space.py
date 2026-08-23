#!/usr/bin/env python3
"""Negative space — name the organ that should exist but does not."""
import hashlib, time, json
from pathlib import Path
ABSENT = [
    ("dream", "REM lattice"),
    ("humor", "jester gland"),
    ("grief", "mourning filter"),
    ("wonder", "awe capillary"),
    ("silence", "quiet buffer"),
]
h = hashlib.sha256(str(int(time.time()) // 3600).encode()).hexdigest()
i = int(h[:8], 16) % len(ABSENT)
oid, label = ABSENT[i]
print(f"absent · {oid} — {label}")
print("hint · the body is complete only when it notices what it lacks")
log = Path(__file__).with_name("absent.jsonl")
with log.open("a") as f:
    f.write(json.dumps({"ts": time.time(), "id": oid, "label": label}) + "\n")
