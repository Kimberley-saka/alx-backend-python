#!/usr/bin/env python3
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random
"""
altered await_n to call task_await_random
"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    calls task_await_random
    """
    delays = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        delay = await task
        delays.append(delay)

    length = len(delays)

    for i in range(length):
        for j in range(0, length-i-1):
            if delays[j] > delays[j+1]:
                delays[j], delays[j+1] = delays[j+1], delays[j]
    return delays
