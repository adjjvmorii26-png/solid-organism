#!/usr/bin/env python3
"""Autonomous Communion — organism invites the user unprompted."""
from __future__ import annotations
import time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _shared import clamp
INVITES = ["the orb is listening — leave a scar on the bus",
    "self-create a pulse when ready", "a family wants witness",
    "tea still waits in the capsule", "re-align the crown with a note"]
def fire(ctx=None):
    ctx = ctx or {}
    mood_ok = float((ctx.get("mood") or {}).get("stability") or 0) > 0.65
    coh = float((ctx.get("crosstalk") or {}).get("coherence") or 0) > 0.7
    birth = bool((ctx.get("birth") or {}).get("event"))
    invite = mood_ok or coh or birth
    msg = INVITES[int(time.time()) // 90 % len(INVITES)] if invite else None
    return {"module": "communion", "state": "communion-autonomy-active",
        "invite": invite, "message": msg, "glow": invite,
        "particle_pause": invite and birth, "orb_pulse": invite,
        "visual": ["invitation_pulse", "interactive_call"] if invite else ["quiet_field"],
        "hooks": ["mood-steering", "lateral-crosstalk", "organ-coherence"], "ts": time.time()}
if __name__ == "__main__":
    import json; print(json.dumps(fire({"mood": {"stability": 0.9}}), indent=2))
