#!/usr/bin/env python3
"""
This module contains an asynchronous generator coroutine.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """
    Loops 10 times, waits 1 second each time, and yields
    a random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
