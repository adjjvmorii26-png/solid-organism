#!/usr/bin/env python3
"""Complexity tracker."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
def measure() -> dict:
    files = list(ROOT.rglob("*"))
    py = [p for p in files if p.suffix == ".py"]
    return {"files": len([p for p in files if p.is_file()]), "py": len(py)}
if __name__ == "__main__":
    print(measure())
