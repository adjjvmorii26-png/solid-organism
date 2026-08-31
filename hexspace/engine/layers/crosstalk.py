#!/usr/bin/env python3
"""Self-Triggered Crosstalk — organ families signal without external input."""
from __future__ import annotations
import time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _shared import rng, clamp
FAMILIES = {"sense-memory": ("sense", "memory"), "guard-immune": ("guard", "immune"),
    "growth-motor": ("growth", "motor"), "bus-cortex": ("bus", "cortex"),
    "cash-meta": ("cashflow", "metabolism")}
def fire(ctx=None):
    r = rng("xtalk")
    family = r.choice(list(FAMILIES))
    a, b = FAMILIES[family]
    conflict, burst = r.random() < 0.25, r.random() < 0.35
    coherence = clamp(0.35 + r.random() * 0.55 - (0.15 if conflict else 0))
    return {"module": "crosstalk", "state": "crosstalk-autonomy-active",
        "family": family, "nodes": [a, b], "conflict": conflict, "burst": burst,
        "coherence": round(coherence, 3),
        "arcs": r.randint(2, 7) if burst else r.randint(1, 3),
        "crown_pulse": burst or coherence > 0.75,
        "particle_dir": r.choice(["inward", "outward", "lateral", "spiral"]),
        "visual": ["arcs_flash", "crown_pulse", "particle_dir_shift"],
        "hooks": ["lateral-crosstalk", "domain-signals", "particle-intelligence"],
        "ts": time.time()}
if __name__ == "__main__":
    import json; print(json.dumps(fire(), indent=2))
