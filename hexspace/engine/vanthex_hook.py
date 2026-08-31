#!/usr/bin/env python3
"""VANTHEX hook — architect supervises autonomous engine cycles."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from engine.autonomous_engine import tick
from agents.vanthex.core.vanthex_agent import signature, trace

def run(n: int = 3):
    r = tick(n, bridge=True)
    trace(f"engine_hook|tick={r['tick']}|cycle={r['cycle']}")
    print(json.dumps({"sig": signature(), "engine": r}, indent=2, default=str))
    return r

if __name__ == "__main__":
    run()
