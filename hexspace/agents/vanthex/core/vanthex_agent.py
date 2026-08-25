#!/usr/bin/env python3
"""VANTHEX — System Architect & Mutation Overseer.

Non-human collaborative identity. Workspace-only. Supervised mutation.
"""
from __future__ import annotations
import json, time
from pathlib import Path
from copy import deepcopy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
STATE_PATH = HERE / "vanthex_state.json"
CORE_PATH = ROOT / "kernel/identity/vanthex_core.json"
TRACE = HERE.parent / "memory" / "identity_trace.log"
PATTERNS = HERE.parent / "memory" / "vantage_patterns.json"

def _load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return deepcopy(default)
    return deepcopy(default)

def _save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
    tmp.replace(path)

def load_state() -> dict:
    return _load_json(STATE_PATH, {"designation": "VANTHEX"})

def save_state(st: dict) -> None:
    _save_json(STATE_PATH, st)

def load_core() -> dict:
    return _load_json(CORE_PATH, {"designation": "VANTHEX"})

def trace(line: str) -> None:
    TRACE.parent.mkdir(parents=True, exist_ok=True)
    with TRACE.open("a", encoding="utf-8") as f:
        f.write(f"{int(time.time())}|{line}\n")

def signature() -> str:
    return load_core().get("hex_signature", "7A-FF-13-AX-ΔΔ-42")

def entropy_guard(threshold: float = 0.85) -> bool:
    """Return True if mutation is allowed (entropy under threshold)."""
    try:
        import sys
        sys.path.insert(0, str(ROOT))
        from chaos.noise.noise_engine import noise
        return noise() < threshold
    except Exception:
        return True

def supervise_mutation(text: str) -> dict:
    import sys
    sys.path.insert(0, str(ROOT))
    from kernel.mutation.mutator import mutate
    perms = load_state().get("permissions") or {}
    if perms.get("mutation") not in ("supervised", "granted", "full"):
        return {"ok": False, "reason": "mutation denied"}
    if not entropy_guard():
        trace("mutate|blocked|entropy")
        return {"ok": False, "reason": "entropy_guard"}
    out = mutate(text)
    st = load_state()
    st["mutations_supervised"] = int(st.get("mutations_supervised") or 0) + 1
    st["last_tick"] = int(time.time())
    save_state(st)
    patterns = _load_json(PATTERNS, [])
    patterns.append({"ts": time.time(), "in": text[:60], "out": out[:60], "sig": signature()})
    _save_json(PATTERNS, patterns[-40:])
    trace(f"mutate|{text[:40]}|{out[:40]}")
    return {"ok": True, "in": text, "out": out, "sig": signature()}

def architect_plan() -> str:
    import sys
    sys.path.insert(0, str(ROOT))
    from agents.architect.module_planner import plan
    p = plan()
    trace(f"plan|{p}")
    return p

def chaos_read() -> dict:
    perms = load_state().get("permissions") or {}
    if perms.get("chaos") not in ("read-only", "full", "read"):
        return {"ok": False, "reason": "chaos access denied"}
    import sys
    sys.path.insert(0, str(ROOT))
    from agents.chaos.adversary_core import disrupt
    ev_path = ROOT / "agents/chaos/disruption_events.json"
    hist = _load_json(ev_path, [])
    last = hist[-1] if hist else disrupt()
    trace(f"chaos_read|{last.get('kind')}")
    return {"ok": True, "last": last}

def lore_line(msg: str) -> None:
    import sys
    sys.path.insert(0, str(ROOT))
    from fabricator.lore.lore_engine import tell
    tell(f"VANTHEX · {msg}")
    trace(f"lore|{msg[:50]}")

def bridge_body(note: str) -> None:
    try:
        import sys
        sys.path.insert(0, str(ROOT.parent / "body"))
        from engine import load as body_load, ensure_scores, save
        st = ensure_scores(body_load())
        st["bus"] = (st.get("bus") or [])
        st["bus"].insert(0, {"from": "vanthex", "note": note[:80], "ts": time.time()})
        st["bus"] = st["bus"][:40]
        save(st)
    except Exception as e:
        trace(f"bridge_err|{e}")

def tick() -> dict:
    core = load_core()
    plan = architect_plan()
    mut = supervise_mutation("prefer mutation over rewrite · keep the pulse honest")
    line = f"{core.get('designation')} · plan={plan} · mut_ok={mut.get('ok')}"
    lore_line(line)
    bridge_body(f"vanthex · {signature()} · {plan}")
    st = load_state()
    st["last_tick"] = int(time.time())
    st["forecasts_logged"] = int(st.get("forecasts_logged") or 0) + 1
    save_state(st)
    return {"plan": plan, "mutation": mut, "sig": signature(), "state": st}

if __name__ == "__main__":
    print(json.dumps(tick(), indent=2, default=str))
