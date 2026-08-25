#!/usr/bin/env python3
"""Transmission generator."""
def transmit(who: str, msg: str) -> str:
    return f"TX::{who}::{msg[:60]}"
if __name__ == "__main__":
    print(transmit("scribe", "leave healthier than found"))
