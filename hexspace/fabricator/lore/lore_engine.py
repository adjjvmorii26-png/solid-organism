#!/usr/bin/env python3
"""Lore engine — append a myth line."""
import time
from pathlib import Path
STORY = Path(__file__).with_name("evolving_story.hex")
def tell(line: str) -> None:
    with STORY.open("a") as f:
        f.write(f"{int(time.time())}|{line}\n")
if __name__ == "__main__":
    tell("hexspace opened a chamber under the organism")
    print("lore · told")
