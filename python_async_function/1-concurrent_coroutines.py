#!/usr/bin/env python3
'''1-concurrent_coroutines.py'''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''wait_n'''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delay_list = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_list.append(delay)

    return delay_list
