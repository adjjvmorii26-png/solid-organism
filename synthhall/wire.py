#!/usr/bin/env python3
"""lattice-wire/1 — trusted room filter."""
TRUSTED = {"stewards", "debate", "lobby"}
def accept(room: str) -> bool:
    return room.lower() in TRUSTED
def stamp(msg: str, who: str) -> dict:
    return {"from": who, "msg": msg, "wire": "lattice-wire/1"}
if __name__ == "__main__":
    print("wire · trusted", sorted(TRUSTED))
