#!/usr/bin/env python3
"""Behavior smoke tests."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from agents.seer.foresight_engine import foresee
from agents.scribe.transmission_generator import transmit
from agents.chaos.adversary_core import disrupt
def main():
    print("beh · seer", foresee()[:40])
    print("beh · tx", transmit("test", "ok"))
    print("beh · chaos", disrupt()["kind"])
if __name__ == "__main__":
    main()
