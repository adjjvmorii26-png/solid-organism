#!/usr/bin/env python3
"""Post a debate claim."""
import argparse, json, time
from pathlib import Path
P = Path(__file__).parent / "data"
P.mkdir(exist_ok=True)
log = P / "hall.jsonl"
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="frm", default="Steward")
    ap.add_argument("--claim", default="prefer mutation over rewrite")
    args = ap.parse_args()
    with log.open("a") as f:
        f.write(json.dumps({"ts": time.time(), "from": args.frm, "claim": args.claim}) + "\n")
    print(f"claim · {args.frm}: {args.claim}")
if __name__ == "__main__":
    main()
