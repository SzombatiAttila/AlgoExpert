# pylint: disable=missing-function-docstring, (missing-module-docstring
import asyncio
import requests

import aiohttp


async def async_ping_google():
    for _ in range(100):
        status_code = requests.get("https://google.com").status_code
        print(f'google status code is : {status_code}')

async def async_ping_facebook():
    for i in range(100):
        status_code = requests.get("https://lensa.com").status_code
        if i in [20, 30]:
            await asyncio.sleep(0.5)
        print(f'lensa status code is : {status_code}')


def get_fibonacci_numbers(number=1000):
    res = []
    first_num, next_num = 0, 1
    res.append(first_num)
    res.append(next_num)
    for _ in range(number):
        print(res)
        first_num, next_num = next_num, first_num + next_num
        res.append(next_num)
        return res

async def main():
    facebook = asyncio.create_task(async_ping_facebook())
    google = asyncio.create_task(async_ping_google())
    await facebook
    await google

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
