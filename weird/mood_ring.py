#!/usr/bin/env python3
"""Mood ring — color from hour."""
import time
colors = ["void", "indigo", "amber", "jade", "crimson", "silver"]
h = time.localtime().tm_hour
print("mood ·", colors[h % len(colors)])
