#!/usr/bin/env python3
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random
"""
Imported wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times
with the specified max_delay. wait_n should return the list of all
the delays (float values). The list of the delays should be in ascending
order without using sort() because of concurrency.
"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns the wait_random function n times and sorts
    the delays
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
