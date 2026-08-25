#!/usr/bin/env python3
"""Paradox seed — two axioms that cannot both be true."""
import json, time
from pathlib import Path
A, B = "the body is complete", "the body is always missing an organ"
tension = abs(hash(A) % 100 - hash(B) % 100) / 100
Path(__file__).with_name("paradox.json").write_text(
    json.dumps({"ts": time.time(), "A": A, "B": B, "tension": round(tension, 3)}, indent=2)
)
print(f"paradox · «{A}» ⟂ «{B}»")
print(f"tension · {tension:.3f}")
