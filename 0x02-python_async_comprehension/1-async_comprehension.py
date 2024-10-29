#!/usr/bin/env python3
"""Python file"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Uses asyc_generator to yeild 10 random float
    and then use asyc comprehension to create a list of the value
    """
    results = [i async for i in async_generator()]
    return results
