#!/usr/bin/env python3
"""IXPANSION body engine — solid-organism core.

Atomic save. Prefer mutation. Leave healthier than found.
"""
from __future__ import annotations
import json, time
from pathlib import Path
from copy import deepcopy

DATA = Path(__file__).resolve().parent / "data"
STATE_PATH = DATA / "body_state.json"


def load() -> dict:
    if not STATE_PATH.exists():
        raise FileNotFoundError(STATE_PATH)
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save(st: dict) -> None:
    DATA.mkdir(exist_ok=True)
    payload = json.dumps(st, indent=2)
    tmp = STATE_PATH.with_suffix(".json.tmp")
    tmp.write_text(payload, encoding="utf-8")
    if STATE_PATH.exists():
        try:
            STATE_PATH.with_suffix(".json.bak").write_text(
                STATE_PATH.read_text(encoding="utf-8"), encoding="utf-8"
            )
        except Exception:
            pass
    tmp.replace(STATE_PATH)


def clamp_organ(score: float) -> float:
    return max(0.4, min(0.99, float(score)))


def body_score(st: dict) -> float:
    organs = st.get("organs") or []
    if not organs:
        return 0.0
    m = sum(float(o.get("score", 0)) for o in organs) / len(organs)
    return round(m * 1000) / 10


def ensure_scores(st: dict) -> dict:
    st = deepcopy(st)
    for o in st.get("organs") or []:
        o["score"] = clamp_organ(o.get("score", 0.85))
    st["body_score"] = body_score(st)
    st.setdefault("bus", [])
    st.setdefault("agents", [])
    return st


def cross_pollinate(st: dict) -> dict:
    organs = st.get("organs") or []
    if len(organs) >= 2:
        i = int(time.time()) % len(organs)
        j = (i + 3) % len(organs)
        organs[j]["score"] = clamp_organ(float(organs[j]["score"]) + 0.005)
    return st


def pulse_cycle_evolution(st: dict) -> dict:
    organs = st.get("organs") or []
    if organs:
        weak = min(organs, key=lambda o: float(o.get("score", 0)))
        weak["score"] = clamp_organ(float(weak["score"]) + 0.01)
    return st


def sky_from_state(st: dict) -> str:
    if st.get("sky_override"):
        return str(st["sky_override"])
    organs = sorted(st.get("organs") or [], key=lambda o: -float(o.get("score", 0)))[:3]
    return "–".join(str(o.get("id", "?")).upper() for o in organs) or "VOID"


def bus_voices(st: dict, limit: int = 12) -> dict:
    tags = {}
    for m in st.get("bus") or []:
        fr = (m.get("from") or "?").lower()
        tags[fr] = tags.get(fr, 0) + 1
    return dict(sorted(tags.items(), key=lambda x: -x[1])[:limit])


def run_pulse(st: dict) -> dict:
    st = ensure_scores(st)
    st = cross_pollinate(st)
    st = pulse_cycle_evolution(st)
    st["body_score"] = body_score(st)
    bus = list(st.get("bus") or [])
    bus.insert(0, {
        "from": "pulse",
        "note": f"pulse · score={st['body_score']} · sky={sky_from_state(st)}",
        "ts": time.time(),
    })
    st["bus"] = bus[:40]
    return st


def creatures(st: dict) -> list:
    return list(st.get("agents") or [])


def integration_checks(st: dict) -> dict:
    checks = []
    checks.append(("has_organs", bool(st.get("organs"))))
    checks.append(("has_agents", bool(st.get("agents"))))
    checks.append(("has_bus", "bus" in st))
    checks.append(("score_range", 0 <= float(st.get("body_score") or 0) <= 100))
    for o in st.get("organs") or []:
        s = float(o.get("score", 0))
        checks.append((f"organ_{o.get('id')}_clamped", 0.4 <= s <= 0.99))
    passed = sum(1 for _, ok in checks if ok)
    return {"passed": passed, "total": len(checks), "checks": checks, "ok": passed == len(checks)}
