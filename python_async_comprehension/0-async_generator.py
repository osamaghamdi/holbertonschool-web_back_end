#!/usr/bin/env python3
"""0-async_generator.py"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """An async generator that yields random float numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
