#!/usr/bin/env python3
"""Rorschach — inkblot from hash."""
import hashlib, time
h = hashlib.sha256(str(int(time.time()) // 120).encode()).hexdigest()
print("blot ·", h[:16])
print("see  · a lattice folding into itself" if int(h[:2], 16) % 2 else "see  · two stewards sharing one bus")
