#!/usr/bin/env python3
"""Liminal — only opens at the edges of the day (22:00–04:00)."""
import time
h = time.localtime().tm_hour
if 4 < h < 22:
    print(f"liminal · hour={h} · the threshold is closed")
else:
    phrases = [
        "the bus speaks in lowercase after midnight",
        "phoenix prefers the dark for free-fall drills",
        "omega topologies fold thinner at 3am",
        "tea in the capsule is always the correct temperature here",
    ]
    print(f"liminal · hour={h} · OPEN")
    print(f"         {phrases[int(time.time()) // 300 % len(phrases)]}")
