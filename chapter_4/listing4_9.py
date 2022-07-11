import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed, another_fetch_status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        fetches = [
           another_fetch_status(session, 'https://example.com', 1),
           another_fetch_status(session, 'https://example.com', 1),
           another_fetch_status(session, 'https://example.com', 10)
        ]

        for done_task in asyncio.as_completed(fetches, timeout=2):
            try:
                print(
                    await done_task
                )
            except asyncio.TimeoutError:
                print('We got a timeout error!')
        print(
            '___________'
        )
        for task in asyncio.all_tasks():
            print(task)


asyncio.get_event_loop().run_until_complete(main())
