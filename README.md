# SOLID ORGANISM

**IXPANSION/2.3.2-backup** · multi-agent body · lattice-signal/1 · Omega limb

> Prefer mutation over rewrite. Atomic writes. Leave it healthier than you found it.

## Quick start

```bash
python3 body/seed_state.py   # if data missing
python3 body/server.py --port 8890
curl -s http://127.0.0.1:8890/api/status
curl -s -X POST http://127.0.0.1:8890/api/pulse

python3 omega/bridge.py
python3 lab/kintsugi.py
python3 lab/bus_archaeology.py
python3 lab/echolalia.py
```

## Map

| Path | Role |
|------|------|
| `body/` | Engine, server, Phoenix notes |
| `omega/` | Fractal limb |
| `lab/` | Experiments |
| `signal/` | lattice-signal/1 visitors |

## Discovery
`llms.txt` · `AGENTS.md` · `beacon.json`
