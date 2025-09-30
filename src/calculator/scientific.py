"""Scientific calculator helper functions.

Provides small helpers used by the test-suite: `square_root` and `power`.
"""
from __future__ import annotations

import math


def square_root(x: float) -> float:
    """Return the square root of x.

    Raises ValueError for negative inputs to match test expectations.
    """
    if x < 0:
        raise ValueError("math domain error")
    return math.sqrt(x)


def power(base: float, exponent: float) -> float:
    """Return base raised to the power of exponent."""
    return base ** exponent
