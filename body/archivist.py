"""Archivist — summarize bus scars."""
def summary(bus: list, limit: int = 5) -> list:
    return [{"from": m.get("from"), "note": (m.get("note") or "")[:60]} for m in (bus or [])[:limit]]
