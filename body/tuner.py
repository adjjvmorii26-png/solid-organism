"""Tuner — organ nudges."""
def tune(organ: dict, delta: float = 0.01) -> dict:
    organ = dict(organ)
    s = float(organ.get("score", 0.8))
    organ["score"] = max(0.4, min(0.99, s + delta))
    return organ
