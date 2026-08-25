#!/usr/bin/env python3
"""Signal encoder."""
def encode(msg: str) -> str:
    return msg.encode().hex()[:64]
if __name__ == "__main__":
    print(encode("leave healthier"))
