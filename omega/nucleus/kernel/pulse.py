import time
_TICK = 0
def tick():
    global _TICK
    _TICK += 1
    return {"tick": _TICK, "ts": time.time()}
