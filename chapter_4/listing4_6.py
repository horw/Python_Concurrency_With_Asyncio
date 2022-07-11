import asyncio
import aiohttp
from aiohttp import ClientSession
from util import fetch_status, async_timed


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            'https://example.com'
            for _ in range(5)
        ] + [
            'python://example.com'
            for _ in range(5)
        ]

        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests, return_exceptions=True)
        print(status_codes)

asyncio.get_event_loop().run_until_complete(main())
