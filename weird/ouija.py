#!/usr/bin/env python3
"""Ouija — answer a question from body noise."""
import hashlib, sys
q = " ".join(sys.argv[1:]) or "what next"
h = hashlib.sha256(q.encode()).hexdigest()
words = ["pulse", "phoenix", "lattice", "scar", "tea", "fork", "aurora", "bus"]
ans = " ".join(words[int(h[i:i+2], 16) % len(words)] for i in range(0, 8, 2))
print(f"ouija · {q}")
print(f"planchette · {ans}")
