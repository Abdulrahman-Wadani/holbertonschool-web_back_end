#!/usr/bin/env python3
'''4-tasks.py'''
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''wait_n'''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay_list = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_list.append(delay)

    return delay_list
