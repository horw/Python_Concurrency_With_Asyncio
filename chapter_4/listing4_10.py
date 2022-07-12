import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed,another_fetch_status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = \
        [
            asyncio.create_task(another_fetch_status(session, 'https://example.com')),
            asyncio.create_task(another_fetch_status(session, 'https://example.com'))
        ]
        done, pending = await asyncio.wait(fetchers)
        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)


asyncio.get_event_loop().run_until_complete(main())