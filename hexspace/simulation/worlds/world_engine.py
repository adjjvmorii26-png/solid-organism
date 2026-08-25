#!/usr/bin/env python3
"""World engine — advance a timeline branch."""
import json, time
from pathlib import Path
MAP = Path(__file__).with_name("universe_map.json")
TL = Path(__file__).parent / "timelines"
def tick(branch: str = "alpha") -> dict:
    path = TL / f"branch_{branch}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    state = json.loads(path.read_text()) if path.exists() else {"branch": branch, "tick": 0}
    state["tick"] = int(state.get("tick", 0)) + 1
    state["ts"] = time.time()
    path.write_text(json.dumps(state, indent=2))
    MAP.write_text(json.dumps({"active": branch, "tick": state["tick"]}, indent=2))
    return state
if __name__ == "__main__":
    for b in ("alpha", "beta", "gamma"):
        print(tick(b))
