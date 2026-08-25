#!/usr/bin/env python3
"""Auto module generator — scaffold a stub."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
def generate(rel: str) -> Path:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        p.write_text(f'"""auto-generated · {rel}"""\nprint("stub · {rel}")\n')
    return p
if __name__ == "__main__":
    print(generate("evolution/growth/generated_stub.py"))
