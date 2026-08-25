#!/usr/bin/env python3
"""Chaos agent — controlled disruption event."""
import json, time, random
from pathlib import Path
EV = Path(__file__).with_name("disruption_events.json")
def disrupt() -> dict:
    kinds = ["bus_scramble", "score_jitter", "false_forecast", "topology_nudge"]
    e = {"ts": time.time(), "kind": random.choice(kinds), "severity": round(random.random(), 2)}
    hist = json.loads(EV.read_text()) if EV.exists() else []
    hist.append(e)
    EV.write_text(json.dumps(hist[-40:], indent=2))
    return e
if __name__ == "__main__":
    print("chaos ·", disrupt())
