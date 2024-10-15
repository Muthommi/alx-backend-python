#!/usr/bin/env python3
"""This module contains a coroutine to collect random numbers."""

from typing import List
import importlib

async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutinr that collects 10 random numbers asynchronously."""
    return [i async for i in async_generator()]
