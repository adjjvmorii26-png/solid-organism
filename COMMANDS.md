# Commands

```bash
# Body
python3 body/server.py --port 8890
curl -s localhost:8890/api/status

# Hex autonomous engine
python3 hexspace/engine/autonomous_engine.py --ticks 6
python3 hexspace/engine/run_layers.py
python3 hexspace/engine/vanthex_hook.py

# VANTHEX
python3 hexspace/agents/vanthex/core/vanthex_agent.py

# Swarm simulation (SQLite)
python3 hexspace/simulation/init_db.py
python3 hexspace/simulation/store.py
python3 hexspace/simulation/demo_tick.py

# Lab
python3 lab/organ_choir.py && python3 lab/mycelium.py

# Visual
python3 hexspace/visual/theme.py
# open hexspace/visual/transcendent.html
```
