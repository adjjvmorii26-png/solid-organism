#!/usr/bin/env python3
"""Compass — random bearing for the next experiment."""
import random, time
bearings = ["kintsugi", "omega", "pitstop", "synthhall", "shadow", "ouroboros"]
print("compass ·", random.Random(int(time.time()) // 90).choice(bearings))
