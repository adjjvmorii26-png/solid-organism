#!/usr/bin/env python3
"""Thin API over the swarm simulation SQLite store."""
from __future__ import annotations
import json, os, sqlite3, time
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
DB_PATH = Path(os.environ.get("IXPANSION_SIM_DB", "/tmp/ixpansion_device.sqlite3"))

def connect(db_path: Path | None = None) -> sqlite3.Connection:
    path = Path(db_path) if db_path else DB_PATH
    if not path.exists():
        from init_db import init
        init(path)
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = DELETE")
    return conn

def list_simulations() -> list[dict]:
    with connect() as conn:
        rows = conn.execute("SELECT * FROM simulations ORDER BY created_at DESC").fetchall()
        return [dict(r) for r in rows]

def get_simulation(sim_id: str) -> dict | None:
    with connect() as conn:
        row = conn.execute(
            "SELECT * FROM simulations WHERE simulation_id = ?", (sim_id,)
        ).fetchone()
        return dict(row) if row else None

def log_snapshot(
    sim_id: str,
    frame: int,
    average_speed: float | None = None,
    cluster_entropy: float | None = None,
    state: bytes | None = None,
) -> int:
    with connect() as conn:
        cur = conn.execute(
            """
            INSERT INTO simulation_snapshots
            (simulation_id, frame_number, timestamp, average_speed, cluster_entropy, serialized_state)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (sim_id, frame, time.time(), average_speed, cluster_entropy, state),
        )
        conn.commit()
        return int(cur.lastrowid)

def log_event(
    sim_id: str,
    frame: int,
    agent_index: int,
    event_type: str,
    payload: dict | str | None = None,
) -> int:
    if isinstance(payload, dict):
        payload = json.dumps(payload)
    with connect() as conn:
        cur = conn.execute(
            """
            INSERT INTO agent_events
            (simulation_id, frame_number, agent_index, event_type, payload)
            VALUES (?, ?, ?, ?, ?)
            """,
            (sim_id, frame, agent_index, event_type, payload),
        )
        conn.commit()
        return int(cur.lastrowid)

def set_status(sim_id: str, status: str) -> None:
    with connect() as conn:
        conn.execute(
            "UPDATE simulations SET status = ? WHERE simulation_id = ?",
            (status, sim_id),
        )
        conn.commit()

def summary(sim_id: str) -> dict[str, Any]:
    with connect() as conn:
        sim = conn.execute(
            "SELECT * FROM simulations WHERE simulation_id = ?", (sim_id,)
        ).fetchone()
        snaps = conn.execute(
            "SELECT COUNT(*) AS n, MAX(frame_number) AS last_frame FROM simulation_snapshots WHERE simulation_id = ?",
            (sim_id,),
        ).fetchone()
        events = conn.execute(
            "SELECT COUNT(*) AS n FROM agent_events WHERE simulation_id = ?",
            (sim_id,),
        ).fetchone()
    return {
        "simulation": dict(sim) if sim else None,
        "snapshots": dict(snaps) if snaps else {},
        "events": dict(events) if events else {},
    }

if __name__ == "__main__":
    print(json.dumps({"sims": list_simulations(), "alpha": summary("sim_gpu_01")}, indent=2))
