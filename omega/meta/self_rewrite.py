from pathlib import Path
import json, time
def propose(change: str):
    p = Path(__file__).resolve().parent / "observers" / "rewrite_log.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a") as f:
        f.write(json.dumps({"ts": time.time(), "change": change}) + "\n")
    return p
