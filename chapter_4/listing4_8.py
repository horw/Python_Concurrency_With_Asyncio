import asyncio
import aiohttp
from aiohttp import ClientSession
from util import another_fetch_status, async_timed


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        fetcher =  [another_fetch_status(session, 'https://example.com',1),
                    another_fetch_status(session, 'https://example.com', 1),
                    another_fetch_status(session, 'https://example.com', 10)]
        for finished_task in asyncio.as_completed(fetcher):
            print(await finished_task)


asyncio.get_event_loop().run_until_complete(main())