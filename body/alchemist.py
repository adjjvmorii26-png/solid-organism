"""Alchemist — small score transformations."""
def transmute(score: float, toward: float = 0.9, rate: float = 0.1) -> float:
    return max(0.4, min(0.99, score * (1 - rate) + toward * rate))
