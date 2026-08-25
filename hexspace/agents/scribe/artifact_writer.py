#!/usr/bin/env python3
"""Scribe — write a short transmission into lore stream."""
import time
from pathlib import Path
LORE = Path(__file__).with_name("lore_stream.hex")
def write(line: str) -> None:
    with LORE.open("a") as f:
        f.write(f"{int(time.time())}|{line}\n")
if __name__ == "__main__":
    write("hexspace online · steward ink")
    print("scribe · inked")
