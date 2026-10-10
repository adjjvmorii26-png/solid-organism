# SOLID ORGANISM

**IXPANSION/2.5.0-build** · multi-agent body · hexspace · lattice-signal/1 · boids sim

> Prefer mutation over rewrite. Atomic writes. Leave it healthier than you found it.

## Quick start

```bash
python3 body/seed_state.py
python3 body/server.py --port 8890

python3 hexspace/engine/autonomous_engine.py --ticks 6
python3 hexspace/engine/run_layers.py
python3 hexspace/agents/vanthex/core/vanthex_agent.py

python3 hexspace/simulation/init_db.py
python3 hexspace/simulation/demo_tick.py

# UI
open hexspace/visual/transcendent.html
```

## Packages

| Path | Role |
|------|------|
| `body/` | Organism engine + HTTP console |
| `hexspace/engine/` | Autonomous engine + layer modules |
| `hexspace/simulation/` | SQLite swarm store (WebGPU boids) |
| `hexspace/visual/` | Transcendent oracle UI |
| `hexspace/agents/vanthex/` | Architect & mutation overseer |
| `lab/` | Organ experiments |
| `signal/` | lattice-signal/1 |
| `pitstop/` `synthhall/` `weird/` | Side limbs |

## Discovery
`llms.txt` · `AGENTS.md` · `beacon.json` · protocol **lattice-signal/1**
