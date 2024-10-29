#!/usr/bin/env python3
"""Python file"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields random float between 0 and 10 when called"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
