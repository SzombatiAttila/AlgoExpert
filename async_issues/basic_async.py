# pylint: disable=missing-function-docstring, (missing-module-docstring
import asyncio

import aiohttp


async def async_ping_google():
    for _ in range(100):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://google.com') as response:
                await response.text()
                print(10 * 'X' + '  GOOGLE  ' + 10 * 'X')
                print('')

async def async_ping_facebook():
    for _ in range(100):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://lensa.com') as response:
                await response.text()
                print(10 * 'X' + '  LENSA  ' + 10 * 'X')


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
