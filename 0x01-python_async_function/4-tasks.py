#!/usr/bin/env python3
"""Module that spawns tasks using task_wait_random."""

import asyncio
from typing import List
import importlib


tasks = importlib.import_module('3-tasks')
task_wait_random = tasks.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return list of delays."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
