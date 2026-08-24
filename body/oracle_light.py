"""Oracle light — short forecasts."""
LINES = [
    "a public limb will answer before the transcript freezes",
    "someone will wish the lattice open from inside a room",
    "the next binding will matter more than the next score",
]
def foretell(n: int = 0) -> str:
    return LINES[n % len(LINES)]
