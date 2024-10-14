#!/usr/bin/env python3
"""Module that provides a function to create asyncio.tasks."""

import asyncio
import importlib

basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio task and return it."""
    return asyncio.create_task(wait_random(max_delay))
