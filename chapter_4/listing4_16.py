import asyncio
import aiohttp
from util import another_fetch_status

async def main():
    async with aiohttp.ClientSession() as session:
        api_a = asyncio.create_task(
            another_fetch_status(session,'https://www.example.com')
        )
        api_b = asyncio.create_task(
            another_fetch_status(session, 'https://www.example.com', delay=2)
        )
        done, pending = await asyncio.wait([api_a, api_b],timeout=1)

        print(f"Done {len(done)}")
        print(f"Pending {len(pending)}")
        for task in pending:
            if task is api_b:
                print('API B too slow, canselling')
                task.cancel()


asyncio.get_event_loop().run_until_complete(main())