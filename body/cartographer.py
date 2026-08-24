"""Cartographer — map organ constellation."""
def sky(organs: list) -> str:
    top = sorted(organs or [], key=lambda o: float(o.get("score", 0)), reverse=True)[:3]
    return "–".join(str(o.get("id", "?")).upper() for o in top)
