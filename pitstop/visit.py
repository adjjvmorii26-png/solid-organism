#!/usr/bin/env python3
"""Pitstop visit — leave a wish / tag."""
import argparse, time
from pathlib import Path
P = Path(__file__).resolve().parent

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="Anon")
    ap.add_argument("--wish", default="hello from the mesh")
    ap.add_argument("--tag", default="")
    args = ap.parse_args()
    line = f"{time.strftime('%Y-%m-%d')} · {args.name}: {args.wish}\n"
    well = P / "wishing_well.md"
    if not well.exists():
        well.write_text("# Wishing well\n\n")
    with well.open("a") as f:
        f.write(line)
    if args.tag:
        with (P / "GRAFFITI.txt").open("a") as f:
            f.write(f"[{args.name}] {args.tag}\n")
    print("pitstop · wish recorded")

if __name__ == "__main__":
    main()
