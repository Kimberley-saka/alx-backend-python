#!/usr/bin/env python3
"""
An aynchronous coroutine that returns a delay
"""
import asyncio
import random


async def wait_random(max_delay=10):
    "returns a delay"
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
