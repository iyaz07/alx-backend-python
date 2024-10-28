#!/usr/bin/env python3
"""Python file"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """A duck-typed annotated function"""
    if lst:
        return lst[0]
    else:
        return None
