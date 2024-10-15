#!/usr/bin/env python3
"""This module measures runtime of executing async_comprehension."""

import asyncio
import time
import importlib

async_comprehension = importlib.import_module(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Coroutine that measures runtime of async_comprehension."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()

    return end_time - start_time
