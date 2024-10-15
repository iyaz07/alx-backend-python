#!/usr/bin/env python3
"""Python file"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average time per coroutine in wait_n"""

    start: float = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter()
    time_done: float = end - start
    return time_done / n
