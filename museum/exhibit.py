#!/usr/bin/env python3
"""Museum — write EXHIBITS.md from body lore."""
from pathlib import Path
out = Path(__file__).parent / "EXHIBITS.md"
out.write_text("""# IXPANSION Museum

## Hall of Free-Fall
Phoenix exists because this hall does.

## Hall of Power
Phoenix · Aether

## Hall of Noise
Jester · Oracle-light

## Hall of Pit
`pitstop/`

## Hall of Signal
lattice-signal/1
""")
print("museum · exhibits refreshed")
