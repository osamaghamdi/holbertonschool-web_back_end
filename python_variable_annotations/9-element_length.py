#!/usr/bin/env python3
"""Returns the length of each element in a list of sequences."""
from typing import Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> Iterable[Tuple[int, int]]:
    """Returns a list of tuples containing the element and its length."""
    return [(i, len(i)) for i in lst]