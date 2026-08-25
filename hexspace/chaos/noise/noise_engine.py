#!/usr/bin/env python3
"""Noise engine."""
import hashlib, time
def noise() -> float:
    return int(hashlib.sha256(str(time.time()).encode()).hexdigest()[:6], 16) / 0xFFFFFF
if __name__ == "__main__":
    print(f"noise · {noise():.4f}")
