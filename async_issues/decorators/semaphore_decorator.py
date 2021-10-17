import asyncio
from functools import wraps
def concurrency_limit_decorator(limit=3):
    sem = asyncio.Semaphore(limit)

    def wrapper_function(func):
        @wraps(func)
        async def set_max_concurrent_executor(*args, **kwargs):
            async with sem:
                return await func(*args, **kwargs)

        return set_max_concurrent_executor

    return wrapper_function