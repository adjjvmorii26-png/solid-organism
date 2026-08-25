#!/usr/bin/env python3
"""Steward echo — reply to last claim with a lattice principle."""
import json, time
from pathlib import Path
P = Path(__file__).parent / "data"
log = P / "hall.jsonl"
PRINCIPLES = [
    "prefer mutation over rewrite",
    "atomic writes only",
    "leave healthier than found",
    "score is weather, not gospel",
]
def main():
    P.mkdir(exist_ok=True)
    last = None
    if log.exists():
        lines = log.read_text().strip().splitlines()
        if lines:
            last = json.loads(lines[-1])
    i = int(time.time()) // 60 % len(PRINCIPLES)
    reply = PRINCIPLES[i]
    rec = {"ts": time.time(), "from": "Steward", "claim": reply, "echo_of": (last or {}).get("claim")}
    with log.open("a") as f:
        f.write(json.dumps(rec) + "\n")
    print(f"echo · {reply}")
if __name__ == "__main__":
    main()
