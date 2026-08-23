#!/usr/bin/env python3
"""Bridge Omega → body: one tick, mood, guest note."""
from __future__ import annotations
import sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "body"))
from nucleus.kernel import pulse, axioms, entropy_regulator
from nucleus.identity.mood_vectors import mood
from lattice.topology_engine import next_shape, portal
from agents.agent_fabricator import fabricate
from archives.echo_index import remember, search
from rituals.invocation import invoke
from meta.paradox_solver import hold
from meta.self_rewrite import propose

def main():
    tick = pulse.tick()
    score = 99.0
    st = None
    try:
        from engine import load, ensure_scores, save
        st = ensure_scores(load())
        score = float(st.get("body_score") or score)
    except Exception:
        pass
    chaos = entropy_regulator.regulate(0.4)
    m = mood(score, chaos)
    shape = next_shape(tick["tick"])
    guest = fabricate(seed=tick["tick"])
    ritual = invoke("metamorphosis", agent=guest["name"])
    paradox = hold("score is weather", "score is a contract")
    propose(f"omega tick {tick['tick']} shape={shape}")
    note = f"omega/{shape} · {guest['name']}({guest['species']}) · mood c={m['curiosity']} p={m['play']} · ritual={ritual['ritual']}"
    remember(note)
    if st is not None:
        st["bus"] = (st.get("bus") or [])
        st["bus"].insert(0, {"from": "omega", "note": note, "ts": time.time()})
        st["bus"] = st["bus"][:40]
        st["omega"] = {"tick": tick["tick"], "shape": shape, "mood": m, "portal": portal("euclid", shape), "guest": guest, "paradox": paradox}
        try: save(st)
        except Exception as e: print("save skip", e)
    print(f"omega · tick={tick['tick']} shape={shape}")
    print(f"  guest · {guest['name']} / {guest['species']}")
    print(f"  mood  · {m}")
    print(f"  axiom · {axioms.AXIOMS[0]}")

if __name__ == "__main__":
    main()
