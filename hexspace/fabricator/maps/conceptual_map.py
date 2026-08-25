#!/usr/bin/env python3
"""Conceptual map — list top-level limbs."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
def limbs():
    return sorted(p.name for p in ROOT.iterdir() if p.is_dir())
if __name__ == "__main__":
    print("map ·", ", ".join(limbs()))
