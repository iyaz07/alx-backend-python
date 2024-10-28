#!/usr/bin/env python3
"""Python file"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies
    a float by multiplier
    """
    return lambda x: multiplier * x
