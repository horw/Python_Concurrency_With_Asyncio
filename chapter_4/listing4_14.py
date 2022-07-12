import asyncio
import aiohttp
from util import async_timed,another_fetch_status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        pending = [asyncio.create_task(another_fetch_status(session,url)),
                   asyncio.create_task(another_fetch_status(session,url)),
                   asyncio.create_task(another_fetch_status(session,url))
                   ]
        while pending:
            done,pending = await asyncio.wait(pending,return_when=asyncio.FIRST_COMPLETED)
            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')

            for done_task in done:
                print(await done_task)

asyncio.get_event_loop().run_until_complete(main())