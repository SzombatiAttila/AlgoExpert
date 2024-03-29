import asyncio
from typing import List

import aiohttp
import requests

from async_issues.decorators.semaphore_decorator import concurrency_limit_decorator
from async_issues.decorators.time_meas_decorator import measure_time, measure_time_sync
from async_issues.utils.generate_emails import random_email_generator


@concurrency_limit_decorator(limit=10)
async def get(session: aiohttp.ClientSession, email: str):
    url = f'http://127.0.0.1:8000/email/{email}'
    print(f"Requesting {url}")
    resp = await session.request('GET', url=url)
    data = await resp.json()
    print(f"Received data for {url}")
    return data


@measure_time
async def get_job_seeker_data_by_email(emails: List[str]):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for email in emails:
            tasks.append(asyncio.ensure_future(get(session=session, email=email)))
        await asyncio.gather(*tasks, )


@measure_time_sync
def normal_request_function(emails: List[str]):
    for email in emails:
        res = requests.get(f'http://127.0.0.1:8000/email/{email}')
        print(res.json())


if __name__ == "__main__":
    email_list = random_email_generator(email_length=10, number_of_emails=100)
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(get_job_seeker_data_by_email(email_list))
    print('X' * 100)
    print('The next one will be a synchronous function call')
    print('X' * 100)
    normal_request_function(email_list)
