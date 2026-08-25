#!/usr/bin/env python3
"""Bridge hexspace → organism body bus."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent / "body"))
from kernel.pulse.heartbeat import beat
from agents.seer.foresight_engine import foresee
from agents.scribe.artifact_writer import write as scribe_write
from simulation.worlds.world_engine import tick
from fabricator.lore.lore_engine import tell

def run():
    b = beat(bridge=True)
    forecast = foresee()
    tick("alpha")
    scribe_write(f"forecast:{forecast[:40]}")
    tell(f"hex tick {b.get('tick')} · {forecast[:50]}")
    print(f"bridge · tick={b.get('tick')} · seer={forecast[:50]}")

if __name__ == "__main__":
    run()
