#!/usr/bin/env python3
"""Module to measure execution time of wait_n."""

import time
import asyncio
import importlib

concurrent_coroutines = importlib.import_module('1-concurrent_coroutines')
wait_n = concurrent_coroutines.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average runtime of wait_n for n times."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
