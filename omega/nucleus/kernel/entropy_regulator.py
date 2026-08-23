def regulate(chaos: float, target: float = 0.35) -> float:
    return max(0.05, min(0.95, chaos * 0.7 + target * 0.3))
