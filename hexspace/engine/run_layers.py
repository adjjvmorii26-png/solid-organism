#!/usr/bin/env python3
"""Run all autonomy layers with context chaining + optional body birth."""
from __future__ import annotations
import json, time, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from layers import mood, crosstalk, recursive, birth, domain, weather, communion

def run(bridge: bool = True) -> dict:
    ctx, results = {}, {}
    for name, mod in [("mood", mood), ("crosstalk", crosstalk), ("recursive", recursive),
                      ("birth", birth), ("domain", domain), ("weather", weather),
                      ("communion", communion)]:
        results[name] = mod.fire(ctx)
        ctx[name] = results[name]
    summary = {
        "climate": results["mood"]["climate"],
        "family": results["crosstalk"]["family"],
        "storm": results["weather"]["storm"],
        "domain_focus": results["domain"]["focus"],
        "birth": results["birth"].get("organ"),
        "invite": results["communion"].get("message"),
        "ts": time.time(),
    }
    snap = HERE / "state" / "layers_snapshot.json"
    snap.parent.mkdir(exist_ok=True)
    snap.write_text(json.dumps({"summary": summary, "layers": results}, indent=2))
    if bridge:
        try:
            sys.path.insert(0, str(HERE.parents[1] / "body"))
            from engine import load, ensure_scores, save
            st = ensure_scores(load())
            note = f"layers · {summary['climate']}/{summary['storm']} · {summary['family']}"
            if summary["birth"]:
                note += f" · birth:{summary['birth']['id']}"
                oid = summary["birth"]["id"]
                organs = st.get("organs") or []
                if oid not in {o.get("id") for o in organs}:
                    organs.append({"id": oid, "label": summary["birth"]["label"],
                                   "score": 0.86, "dream": True, "born": time.time()})
                    st["organs"] = organs
            if summary["invite"]:
                note += " · communion open"
            st["bus"] = (st.get("bus") or [])
            st["bus"].insert(0, {"from": "hex.layers", "note": note[:90], "ts": time.time()})
            st["bus"] = st["bus"][:40]
            save(ensure_scores(st))
        except Exception as e:
            summary["bridge_err"] = str(e)
    return summary

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
