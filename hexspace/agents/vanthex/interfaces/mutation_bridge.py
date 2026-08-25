#!/usr/bin/env python3
"""Mutation bridge — supervised text mutation."""
import sys, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from agents.vanthex.core.vanthex_agent import supervise_mutation

def run(text: str) -> dict:
    r = supervise_mutation(text)
    print(f"mutation_bridge · ok={r.get('ok')}")
    if r.get("ok"):
        print(f"  in  · {r.get('in')}")
        print(f"  out · {r.get('out')}")
    return r

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", default="prefer mutation over rewrite")
    args = ap.parse_args()
    run(args.text)
