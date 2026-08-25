#!/usr/bin/env python3
"""Architect — propose next module from gaps."""
GAPS = ["observatory.dashboard", "chaos.hostile_agent", "evolution.auto_module"]
def plan() -> str:
    import time
    return GAPS[int(time.time()) // 300 % len(GAPS)]
if __name__ == "__main__":
    print("architect · next →", plan())
