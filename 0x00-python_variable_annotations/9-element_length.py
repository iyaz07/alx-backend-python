#!/usr/bin/env python3
"""Python file"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function to annotate"""
    return [(i, len(i)) for i in lst]
