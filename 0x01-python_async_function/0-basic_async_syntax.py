#!/usr/bin/env python3
"""Python file"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously wait for a random delay between 0 and max_delay seconds.

    Param:
        max_delay (int): The maximum amount of time to wait. Default is 10.

    Returns:
        float: The amount of time waited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay