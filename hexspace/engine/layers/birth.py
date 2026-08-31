#!/usr/bin/env python3
"""Idle Organ Birth — may spawn dream/humor/wonder/myth organs unprompted."""
from __future__ import annotations
import time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _shared import rng, clamp
CANDIDATES = [("dream", "REM lattice"), ("humor", "jester gland"),
    ("wonder", "awe capillary"), ("silence", "quiet buffer"),
    ("myth", "story marrow"), ("compass", "bearing node")]
def fire(ctx=None):
    ctx = ctx or {}
    mood = float((ctx.get("mood") or {}).get("stability") or 0.6)
    coh = float((ctx.get("crosstalk") or {}).get("coherence") or 0.5)
    sent = float((ctx.get("mood") or {}).get("sentience") or 0.5)
    resonance = clamp((mood + coh + sent) / 3)
    p = clamp(0.02 + resonance * 0.2)
    r = rng("birth")
    event = r.random() < p
    pick = r.choice(CANDIDATES) if event else None
    return {"module": "birth", "state": "idle-birth-autonomy-active",
        "probability": round(p, 3), "resonance": round(resonance, 3),
        "event": event, "organ": {"id": pick[0], "label": pick[1]} if pick else None,
        "visual": ["birth_ripple", "organ_announce"] if event else ["idle_hum"],
        "hooks": ["genesis-forge", "resonance-forge", "domain-creation"], "ts": time.time()}
if __name__ == "__main__":
    import json; print(json.dumps(fire(), indent=2))
