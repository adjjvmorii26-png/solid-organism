#!/usr/bin/env python3
"""Hex Autonomous Engine — mood, crosstalk, genesis, domain, weather, communion.

ENDING: autonomous-engine-active
"""
from __future__ import annotations
import json, time, math, random
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE_PATH = HERE / "state" / "engine_state.json"
HEX_ROOT = HERE.parent
BODY = HEX_ROOT.parent / "body"

TRANSITIONS = {
    "mood-cycle": "crosstalk-cycle",
    "crosstalk-cycle": "recursive-cycle",
    "recursive-cycle": "domain-drift",
    "domain-drift": "weather-cycle",
    "weather-cycle": "communion-cycle",
    "communion-cycle": "mood-cycle",
}

def _load() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"mode": "living", "cycle": "mood-cycle", "tick": 0, "layers": {}, "transitions": []}

def _save(st: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(st, indent=2))
    tmp.replace(STATE_PATH)

def _rng(seed_extra: str = "") -> random.Random:
    return random.Random(int(time.time()) // 15 ^ hash(seed_extra) & 0xFFFFFFFF)

def layer_mood(st: dict) -> dict:
    L = st["layers"].setdefault("mood", {})
    phase = (math.sin(time.time() / 45) + 1) / 2
    L["phase"] = round(phase, 3)
    L["stability"] = round(0.55 + 0.4 * (1 - abs(phase - 0.5) * 2), 3)
    L["breathing"] = round(0.8 + 0.4 * phase, 2)
    L["orb_hue"] = int(phase * 360)
    L["state"] = "mood-cycle-active"
    return {"layer": "mood", "phase": L["phase"], "stability": L["stability"], "hue": L["orb_hue"]}

def layer_crosstalk(st: dict) -> dict:
    L = st["layers"].setdefault("crosstalk", {})
    rng = _rng("xtalk")
    L["coherence"] = round(0.4 + rng.random() * 0.5, 3)
    L["crown_pulse"] = rng.random() > 0.6
    L["arcs"] = rng.randint(1, 5)
    L["state"] = "crosstalk-cycle-active"
    return {"layer": "crosstalk", "coherence": L["coherence"], "pulse": L["crown_pulse"], "arcs": L["arcs"]}

def layer_recursive(st: dict) -> dict:
    L = st["layers"].setdefault("recursive", {})
    L["audits"] = int(L.get("audits") or 0) + 1
    L["halo"] = round(0.5 + 0.5 * math.sin(L["audits"] / 3), 3)
    L["gyph"] = round(min(1.0, 0.3 + L["audits"] * 0.02), 3)
    L["state"] = "recursive-cycle-active"
    return {"layer": "recursive", "audits": L["audits"], "halo": L["halo"], "gyph": L["gyph"]}

def layer_birth(st: dict) -> dict:
    L = st["layers"].setdefault("birth", {})
    mood_st = (st["layers"].get("mood") or {}).get("stability", 0.5)
    coherent = (st["layers"].get("crosstalk") or {}).get("coherence", 0.5)
    p = max(0.01, min(0.25, (mood_st * coherent) * 0.2))
    L["probability"] = round(p, 3)
    born = _rng("birth").random() < p
    L["born"] = born
    L["state"] = "idle-birth-cycle-active"
    return {"layer": "birth", "probability": p, "event": born}

def layer_domain(st: dict) -> dict:
    L = st["layers"].setdefault("domain", {})
    rng = _rng("domain")
    L["activity"] = round(0.3 + rng.random() * 0.6, 3)
    L["border"] = round(1.0 + L["activity"], 2)
    L["state"] = "domain-drift-cycle-active"
    return {"layer": "domain", "activity": L["activity"], "border": L["border"]}

def layer_weather(st: dict) -> dict:
    L = st["layers"].setdefault("weather", {})
    mood = (st["layers"].get("mood") or {}).get("phase", 0.5)
    wind = (st["layers"].get("crosstalk") or {}).get("coherence", 0.5)
    pressure = (st["layers"].get("recursive") or {}).get("halo", 0.5)
    L["temperature"] = round(mood, 3)
    L["wind"] = round(wind, 3)
    L["pressure"] = round(pressure, 3)
    L["density"] = round((mood + wind + pressure) / 3, 3)
    L["state"] = "weather-cycle-active"
    return {"layer": "weather", "temp": L["temperature"], "wind": L["wind"], "density": L["density"]}

def layer_communion(st: dict) -> dict:
    L = st["layers"].setdefault("communion", {})
    mood_ok = (st["layers"].get("mood") or {}).get("stability", 0) > 0.65
    birth = (st["layers"].get("birth") or {}).get("born", False)
    invite = bool(mood_ok or birth)
    L["invite"] = invite
    L["glow"] = invite
    L["state"] = "communion-cycle-active"
    return {"layer": "communion", "invite": invite, "glow": invite}

LAYERS = {
    "mood-cycle": layer_mood,
    "crosstalk-cycle": layer_crosstalk,
    "recursive-cycle": layer_recursive,
    "domain-drift": layer_domain,
    "weather-cycle": layer_weather,
    "communion-cycle": layer_communion,
}

def advance(st: dict) -> dict:
    cycle = st.get("cycle") or "mood-cycle"
    fn = LAYERS.get(cycle, layer_mood)
    result = fn(st)
    if cycle != "mood-cycle":
        layer_birth(st)
    nxt = TRANSITIONS.get(cycle, "mood-cycle")
    st["transitions"] = (st.get("transitions") or [])[-19:]
    st["transitions"].append({"from": cycle, "to": nxt, "ts": time.time(), "result": result})
    st["cycle"] = nxt
    st["tick"] = int(st.get("tick") or 0) + 1
    st["mode"] = "living"
    st["ending"] = "autonomous-engine-active"
    return result

def bridge_body(note: str) -> None:
    try:
        import sys
        sys.path.insert(0, str(BODY))
        from engine import load, ensure_scores, save
        bst = ensure_scores(load())
        bst["bus"] = (bst.get("bus") or [])
        bst["bus"].insert(0, {"from": "hex.engine", "note": note[:90], "ts": time.time()})
        bst["bus"] = bst["bus"][:40]
        save(bst)
    except Exception:
        pass

def tick(n: int = 1, bridge: bool = True) -> dict:
    st = _load()
    last = None
    for _ in range(max(1, n)):
        last = advance(st)
    _save(st)
    note = f"hex.engine · tick={st['tick']} · cycle={st['cycle']} · {last}"
    if bridge:
        bridge_body(note[:90])
    return {"tick": st["tick"], "cycle": st["cycle"], "last": last, "layers": st["layers"], "ending": "autonomous-engine-active"}

def status() -> dict:
    st = _load()
    return {
        "mode": st.get("mode"),
        "cycle": st.get("cycle"),
        "tick": st.get("tick"),
        "layers": {k: {kk: vv for kk, vv in v.items() if kk != "state"} for k, v in (st.get("layers") or {}).items()},
        "ending": st.get("ending", "autonomous-engine-active"),
    }

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticks", type=int, default=6)
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--no-bridge", action="store_true")
    args = ap.parse_args()
    if args.status:
        print(json.dumps(status(), indent=2))
    else:
        print(json.dumps(tick(args.ticks, bridge=not args.no_bridge), indent=2, default=str))
