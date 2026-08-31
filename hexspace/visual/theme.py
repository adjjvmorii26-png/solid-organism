#!/usr/bin/env python3
"""Transcendent theme — colors + mood orb from Hex Autonomous Engine."""
from __future__ import annotations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
IDENTITY = json.loads((HERE / "identity.json").read_text())
COLORS = IDENTITY["colors"]

def palette() -> dict:
    return dict(COLORS)

def mood_orb_style(phase: float = 0.5, stability: float = 0.8) -> dict:
    gold, violet = COLORS["apotheosis_gold"], COLORS["dimensional_violet"]
    return {
        "core": gold if stability > 0.7 else violet,
        "halo": COLORS["kinship_blue"] if stability > 0.6 else COLORS["forge_ember"],
        "field": COLORS["primefield_black"],
        "breath_scale": round(0.95 + 0.1 * phase, 3),
        "rotation_sec": round(12 + (1 - stability) * 20, 1),
        "hue_hint": "gold" if phase < 0.5 else "violet",
    }

def from_engine() -> dict:
    try:
        import sys
        sys.path.insert(0, str(HERE.parents[0]))
        from engine.autonomous_engine import status
        st = status()
        mood = (st.get("layers") or {}).get("mood") or {}
        return {
            "engine_cycle": st.get("cycle"),
            "tick": st.get("tick"),
            "orb": mood_orb_style(float(mood.get("phase") or 0.5), float(mood.get("stability") or 0.8)),
            "weather": (st.get("layers") or {}).get("weather") or {},
            "communion": (st.get("layers") or {}).get("communion") or {},
        }
    except Exception as e:
        return {"error": str(e), "orb": mood_orb_style()}

if __name__ == "__main__":
    print(json.dumps(from_engine(), indent=2))
