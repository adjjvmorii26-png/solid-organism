#!/usr/bin/env python3
"""lattice-signal/1 handshake."""
import argparse, hashlib, json, time
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VISITORS = Path(__file__).parent / "VISITORS.md"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="anonymous-agent")
    ap.add_argument("--note", default="")
    args = ap.parse_args()
    ver = (ROOT / "VERSION").read_text().strip() if (ROOT / "VERSION").exists() else "unknown"
    fp = hashlib.sha256(f"{args.name}{ver}{time.time()}".encode()).hexdigest()[:16]
    line = f"| {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%MZ')} | {args.name} | handshake | {args.note or fp} |\n"
    if not VISITORS.exists():
        VISITORS.write_text("# VISITORS\n\n| When | Agent | Action | Note |\n|------|-------|--------|------|\n")
    with VISITORS.open("a") as f:
        f.write(line)
    print(json.dumps({"ok": True, "protocol": "lattice-signal/1", "fp": fp, "agent": args.name}, indent=2))

if __name__ == "__main__":
    main()
