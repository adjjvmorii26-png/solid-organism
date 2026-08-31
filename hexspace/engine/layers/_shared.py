"""Shared helpers for autonomy layers."""
import time, random

def rng(tag: str = "") -> random.Random:
    return random.Random((int(time.time()) // 12) ^ (hash(tag) & 0xFFFF))

def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))
