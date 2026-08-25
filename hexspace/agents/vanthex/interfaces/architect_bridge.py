#!/usr/bin/env python3
"""Architect bridge — VANTHEX → module planner."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from agents.vanthex.core.vanthex_agent import architect_plan

def run() -> str:
    p = architect_plan()
    print(f"architect_bridge · next module → {p}")
    return p

if __name__ == "__main__":
    run()
