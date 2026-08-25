#!/usr/bin/env python3
"""Hexspace heartbeat — tick + optional organism bridge."""
import json, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
PROFILE = HERE / "load_profile.json"

def beat(bridge: bool = True) -> dict:
    now = time.time()
    profile = {
        "ts": now,
        "tick": int(now) // 10,
        "cpu_metaphor": round(0.2 + (int(now) % 50) / 100, 2),
        "status": "alive",
    }
    PROFILE.write_text(json.dumps(profile, indent=2))
    if bridge:
        try:
            import sys
            sys.path.insert(0, str(HERE.parents[2] / "body"))
            from engine import load as body_load, ensure_scores, save
            st = ensure_scores(body_load())
            st["bus"] = (st.get("bus") or [])
            st["bus"].insert(0, {"from": "hex.pulse", "note": f"heartbeat · tick={profile['tick']}", "ts": now})
            st["bus"] = st["bus"][:40]
            save(st)
        except Exception as e:
            profile["bridge_err"] = str(e)
    return profile

if __name__ == "__main__":
    print(json.dumps(beat(), indent=2))
