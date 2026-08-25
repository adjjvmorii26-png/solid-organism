#!/usr/bin/env python3
"""Chaos bridge — read-only disruption peek."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from agents.vanthex.core.vanthex_agent import chaos_read

def run() -> dict:
    r = chaos_read()
    print(json.dumps(r, indent=2, default=str))
    return r

if __name__ == "__main__":
    run()
