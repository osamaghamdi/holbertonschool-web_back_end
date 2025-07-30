#!/usr/bin/env python3
"""Computes the floor of a float number."""


def floor(n: float) -> int:
    """Returns the floor of a float number."""
    return int(n) if n > 0 else int(n) - 1
