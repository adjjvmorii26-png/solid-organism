#!/usr/bin/env python3
"""Random event generator."""
import json, time, random
from pathlib import Path
PROF = Path(__file__).with_name("event_profiles.json")
def event() -> dict:
    profiles = json.loads(PROF.read_text()) if PROF.exists() else ["glitch"]
    return {"ts": time.time(), "event": random.choice(profiles)}
if __name__ == "__main__":
    print(event())
