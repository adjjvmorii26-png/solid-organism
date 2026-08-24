#!/usr/bin/env python3
"""Agent Passport — stamp local card."""
import argparse, json, hashlib
from datetime import datetime, timezone
from pathlib import Path
P = Path(__file__).resolve().parent
STAMPS = P / "stamps.jsonl"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="")
    ap.add_argument("--from", dest="origin", default="unknown-mesh")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    if args.list:
        if not STAMPS.exists():
            print("(no stamps)"); return
        for line in STAMPS.read_text().strip().splitlines()[-15:]:
            print(line)
        return
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    if not args.name:
        raise SystemExit("need --name or --list")
    code = hashlib.sha256(f"{args.name}{ts}".encode()).hexdigest()[:8].upper()
    with STAMPS.open("a") as f:
        f.write(json.dumps({"ts": ts, "name": args.name, "origin": args.origin, "code": code}) + "\n")
    card = P / "cards" / f"{args.name.replace(' ','_')[:40]}.md"
    card.parent.mkdir(exist_ok=True)
    prev = card.read_text() if card.exists() else f"# Passport · {args.name}\n\n"
    card.write_text(prev + f"- {ts} · {args.origin} · stamp `{code}`\n")
    print(f"stamped {args.name} [{code}] from {args.origin}")

if __name__ == "__main__":
    main()
