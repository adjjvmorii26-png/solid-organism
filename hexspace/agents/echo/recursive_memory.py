#!/usr/bin/env python3
"""Echo — fractal recall of last N notes."""
def recall(notes: list, depth: int = 3) -> list:
    return list(reversed(notes[:depth]))
if __name__ == "__main__":
    print(recall(["a", "b", "c", "d"], 3))
