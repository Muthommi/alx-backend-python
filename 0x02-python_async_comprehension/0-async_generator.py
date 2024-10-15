#!/usr/bin/env python3
"""This module contains a coroutine generating random numbers."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Cororutine that asynchronously yields random numbers."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
