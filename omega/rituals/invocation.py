def invoke(name: str, **kw):
    name = name.lower()
    if name in ("convergence", "diverge", "divergence", "metamorphosis"):
        return {"ritual": name, "ok": True, "payload": kw}
    return {"ritual": name, "ok": False, "reason": "unknown"}
