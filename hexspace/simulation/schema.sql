PRAGMA journal_mode = DELETE;
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS simulations (
    simulation_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    agent_count INTEGER NOT NULL,
    max_speed REAL NOT NULL,
    max_force REAL NOT NULL,
    align_weight REAL NOT NULL,
    cohere_weight REAL NOT NULL,
    separate_weight REAL NOT NULL,
    status TEXT DEFAULT 'initialized'
);

CREATE TABLE IF NOT EXISTS simulation_snapshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    simulation_id TEXT NOT NULL,
    frame_number INTEGER NOT NULL,
    timestamp REAL NOT NULL,
    average_speed REAL,
    cluster_entropy REAL,
    serialized_state BLOB,
    FOREIGN KEY (simulation_id) REFERENCES simulations(simulation_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS agent_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    simulation_id TEXT NOT NULL,
    frame_number INTEGER NOT NULL,
    agent_index INTEGER NOT NULL,
    event_type TEXT NOT NULL,
    payload TEXT,
    logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (simulation_id) REFERENCES simulations(simulation_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_snapshots_sim_frame ON simulation_snapshots(simulation_id, frame_number);
CREATE INDEX IF NOT EXISTS idx_events_sim_agent ON agent_events(simulation_id, agent_index);
