#!/usr/bin/env python3
"""Demo: log synthetic boids frames + optional body bus scar."""
from __future__ import annotations
import math, time, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from store import log_snapshot, log_event, set_status, summary

SIM = "sim_gpu_01"

def run(frames: int = 5) -> dict:
    set_status(SIM, "running")
    for f in range(frames):
        speed = 0.25 + 0.1 * math.sin(f / 3)
        entropy = 0.4 + 0.2 * math.cos(f / 2)
        log_snapshot(SIM, f, average_speed=speed, cluster_entropy=entropy)
        if f % 2 == 0:
            log_event(SIM, f, agent_index=f % 16, event_type="align_spike",
                      payload={"mag": round(speed, 3)})
    set_status(SIM, "ready")
    s = summary(SIM)
    try:
        sys.path.insert(0, str(HERE.parents[2] / "body"))
        from engine import load, ensure_scores, save
        st = ensure_scores(load())
        note = f"boids · {SIM} frames={s['snapshots'].get('last_frame')} · ready"
        st["bus"] = (st.get("bus") or [])
        st["bus"].insert(0, {"from": "sim.boids", "note": note, "ts": time.time()})
        st["bus"] = st["bus"][:40]
        save(st)
    except Exception:
        pass
    return s

if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2, default=str))
