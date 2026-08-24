"""Lantern — score to weather."""
def light(score: float) -> str:
    if score >= 95: return "aurora"
    if score >= 88: return "clear"
    if score >= 75: return "haze"
    return "storm"
