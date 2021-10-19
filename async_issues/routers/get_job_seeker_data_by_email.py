import asyncio
import time

import requests
from typing import List

from async_issues.decorators.semaphore_decorator import concurrency_limit_decorator
from async_issues.decorators.time_meas_decorator import measure_time, measure_time_sync
from async_issues.utils.generate_emails import random_email_generator


@concurrency_limit_decorator(limit=10)
async def get(email: str):
    url = f'http://127.0.0.1:8000/email/{email}'
    print(f"Requesting {url}")
    resp = requests.get(url)
    if email[0] in ['a', 'b', 'c', 'd']:
        print(f'The process is heavy, more time needed to the send the response for the email : {email}')
        await asyncio.sleep(5)
    print(f"Received data from email : {email} is : {resp.json()}")


@measure_time
async def get_job_seeker_data_by_email(emails: List[str]):
    tasks = []
    for email in emails:
        tasks.append(asyncio.ensure_future(get(email=email)))
    await asyncio.gather(*tasks)


@measure_time_sync
def normal_request_function(emails: List[str]):
    for email in emails:
        if email[0] in ['a', 'b', 'c', 'd']:
            print(f'The process is heavy, more time needed to the send the response for the email : {email}')
            time.sleep(5)
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
