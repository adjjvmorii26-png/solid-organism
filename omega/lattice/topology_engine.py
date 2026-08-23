SHAPES = ("euclid", "non_euclid", "hyperbolic")
def next_shape(pulse_n: int) -> str:
    return SHAPES[pulse_n % len(SHAPES)]
def portal(from_dim: str, to_dim: str) -> str:
    return f"portal::{from_dim}->{to_dim}"
