#!/usr/bin/env python3
"""Dual pendulum — two moods in antiphase."""
import math, time
t = time.time()
a = (math.sin(t / 30) + 1) / 2
b = 1 - a
print(f"pendulum · curiosity={a:.2f}  caution={b:.2f}")
