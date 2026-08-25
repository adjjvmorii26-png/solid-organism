#!/usr/bin/env python3
"""Dashboard — one-screen hexspace status."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from observatory.metrics.complexity_tracker import measure
from kernel.pulse.heartbeat import beat
def show():
    m = measure()
    b = beat(bridge=False)
    print("══ HEXSPACE DASHBOARD ══")
    print(f"files={m['files']}  py={m['py']}  tick={b.get('tick')}")
    umap = ROOT / "simulation/worlds/universe_map.json"
    if umap.exists():
        print("universe", umap.read_text().strip())
if __name__ == "__main__":
    show()
