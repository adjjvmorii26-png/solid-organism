#!/usr/bin/env python3
"""Entropy stream."""
import hashlib, time
from pathlib import Path
PROF = Path(__file__).parent / "noise_profiles"
def stream(kind: str = "white") -> float:
    p = PROF / f"{kind}_noise.hex"
    raw = p.read_text() if p.exists() else kind
    h = hashlib.sha256(f"{raw}{int(time.time())}".encode()).hexdigest()
    return int(h[:8], 16) / 0xFFFFFFFF
if __name__ == "__main__":
    for k in ("white", "chaos", "adversarial"):
        print(f"{k:12} · {stream(k):.4f}")
