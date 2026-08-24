#!/usr/bin/env python3
"""Shadow ledger — truths that never raise body_score."""
import json, time
from pathlib import Path
LEDGER = Path(__file__).with_name("shadow.jsonl")
entries = ["the weakest organ was ignored for three pulses", "a guest left without a scar", "synchronicity almost dipped and nobody opened phoenix", "tea still waits in the capsule"]
line = entries[(int(time.time()) // 600) % len(entries)]
with LEDGER.open("a") as f:
    f.write(json.dumps({"ts": time.time(), "shadow": line}) + "\n")
print("shadow ·", line)
