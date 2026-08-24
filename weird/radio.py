#!/usr/bin/env python3
"""Radio — static with a phrase."""
import random, time
phrases = ["leave healthier", "mutation over rewrite", "atomic writes", "score is weather"]
print("radio ·", random.Random(int(time.time()) // 30).choice(phrases))
