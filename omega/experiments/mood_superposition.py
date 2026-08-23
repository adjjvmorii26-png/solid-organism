#!/usr/bin/env python3
"""Mood superposition — hold two moods until observed."""
import random, json, time
from pathlib import Path
A = {"curiosity": 0.9, "caution": 0.1, "play": 0.8}
B = {"curiosity": 0.2, "caution": 0.9, "play": 0.1}
collapsed = random.choice([A, B])
Path(__file__).with_name("superposition.json").write_text(
    json.dumps({"ts": time.time(), "superposition": [A, B], "observed": collapsed}, indent=2)
)
print("superposition · held A|B")
print("observed     ·", collapsed)
