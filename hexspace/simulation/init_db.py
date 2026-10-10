#!/usr/bin/env python3
"""Initialize swarm simulation SQLite store + default WebGPU boids profile."""
from __future__ import annotations
import os, sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent
DB_PATH = Path(os.environ.get("IXPANSION_SIM_DB", "/tmp/ixpansion_device.sqlite3"))
SCHEMA = (HERE / "schema.sql").read_text()

DEFAULT = (
    "sim_gpu_01",
    "WebGPU Boids Swarm Alpha",
    4096,
    0.4,
    0.1,
    0.8,
    0.5,
    1.2,
    "ready",
)

def init(db_path: Path | None = None) -> Path:
    path = Path(db_path) if db_path else DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    try:
        conn.executescript(SCHEMA)
        conn.execute(
            """
            INSERT OR REPLACE INTO simulations
            (simulation_id, name, agent_count, max_speed, max_force,
             align_weight, cohere_weight, separate_weight, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            DEFAULT,
        )
        conn.commit()
    finally:
        conn.close()
    return path

if __name__ == "__main__":
    p = init()
    print(f"db · {p}")
    print("profile · sim_gpu_01 · WebGPU Boids Swarm Alpha · 4096 agents · ready")
