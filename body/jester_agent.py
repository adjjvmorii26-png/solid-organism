"""Jester — bus humor."""
JOKES = [
    "phoenix walks into a bar; bartender says we don't serve resurrected scores",
    "82 and 99 meet in the middle and call it weather",
    "atomic writes are a love language",
]
def joke(n: int = 0) -> str:
    return JOKES[n % len(JOKES)]
