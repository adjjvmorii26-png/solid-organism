# Commands

```bash
# Body
python3 body/server.py --port 8890
curl -s localhost:8890/api/status

# Hex autonomous engine
python3 hexspace/engine/autonomous_engine.py --ticks 6
python3 hexspace/engine/run_layers.py

# VANTHEX
python3 hexspace/agents/vanthex/core/vanthex_agent.py

# Swarm simulation
python3 hexspace/simulation/init_db.py
python3 hexspace/simulation/demo_tick.py

# 5D Manifold Reactor (WebGL)
open hexspace/visual/manifold_reactor.html
# or: python3 -m http.server 8765  →  /hexspace/visual/manifold_reactor.html

# Visual theme
python3 hexspace/visual/theme.py
open hexspace/visual/transcendent.html
```
