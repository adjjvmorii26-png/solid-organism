#!/usr/bin/env python3
"""Seed a minimal body_state if missing."""
import json, time
from pathlib import Path
DATA = Path(__file__).resolve().parent / "data"
STATE = DATA / "body_state.json"
ORGANS = ["cortex","immune","memory","metabolism","cashflow","sense","motor","growth","guard","bus"]
def main():
    DATA.mkdir(exist_ok=True)
    if STATE.exists():
        print("seed · already present"); return
    st = {
        "version": "IXPANSION/2.3.2-backup",
        "body_score": 99.0,
        "organs": [{"id": o, "label": o.title(), "score": 0.90} for o in ORGANS],
        "agents": [{"id": "steward", "name": "Steward", "role": "steward"}],
        "bus": [{"from": "steward", "note": "seeded solid-organism", "ts": time.time()}],
    }
    STATE.write_text(json.dumps(st, indent=2))
    print("seed · wrote", STATE)
if __name__ == "__main__":
    main()
