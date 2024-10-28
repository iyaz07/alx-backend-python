#!/usr/bin/env python3
"""python file"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A type annotated function that takes k(str) and v(int or float) and
    return a tuple
    """
    return (k, v * v)
