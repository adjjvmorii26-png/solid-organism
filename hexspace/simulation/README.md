# Swarm Simulation Store

SQLite persistence for WebGPU / boids-style swarm runs.

```bash
python3 hexspace/simulation/init_db.py
python3 hexspace/simulation/store.py
python3 hexspace/simulation/demo_tick.py
```

Tables: `simulations` · `simulation_snapshots` · `agent_events`  
Default: **sim_gpu_01** — WebGPU Boids Swarm Alpha · 4096 agents  
DB path: `$IXPANSION_SIM_DB` or `/tmp/ixpansion_device.sqlite3`
