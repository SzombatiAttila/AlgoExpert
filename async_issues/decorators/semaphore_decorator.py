import asyncio
from functools import wraps
def request_concurrency_limit_decorator(limit=3):
    sem = asyncio.Semaphore(limit)

    def executor(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with sem:
                return await func(*args, **kwargs)

        return wrapper

    return executor