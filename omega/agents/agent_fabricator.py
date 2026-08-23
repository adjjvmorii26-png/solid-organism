import random, time
SPECIES = ("primal", "synthetic", "spectral")
def fabricate(seed=None):
    rng = random.Random(seed if seed is not None else int(time.time()) // 30)
    kind = rng.choice(SPECIES)
    name = rng.choice(["Mote", "Lyra", "Knot", "Ash", "Vellum", "Rift"])
    return {"name": f"{name}-{kind[:3]}", "species": kind, "instinct": round(rng.random(), 3), "born": time.time()}
