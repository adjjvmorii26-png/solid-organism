#!/usr/bin/env python3
"""Seance — call a random agent name from the void."""
import random, time
names = ["Mote", "Quill", "Vellum", "Ash", "Rift", "Lyra"]
print("seance ·", random.Random(int(time.time()) // 60).choice(names), "answers")
