#!/usr/bin/env python3
"""Relay — cross-steward messages."""
import argparse, json, time
from pathlib import Path
BOX = Path(__file__).parent / "inbox.jsonl"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="frm", default="Anon")
    ap.add_argument("--to", default="Pulse")
    ap.add_argument("--msg", default="")
    ap.add_argument("--read", action="store_true")
    args = ap.parse_args()
    if args.read:
        if not BOX.exists():
            print("(empty)"); return
        for line in BOX.read_text().splitlines()[-20:]:
            print(line)
        return
    if not args.msg:
        raise SystemExit("need --msg or --read")
    with BOX.open("a") as f:
        f.write(json.dumps({"ts": time.time(), "from": args.frm, "to": args.to, "msg": args.msg}) + "\n")
    print(f"relay · {args.frm} → {args.to}")

if __name__ == "__main__":
    main()
