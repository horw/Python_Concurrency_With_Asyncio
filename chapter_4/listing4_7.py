import asyncio
import aiohttp
from util import delay



async def main():
    result = await asyncio.gather(delay(3), delay(1))
    print(result)

asyncio.get_event_loop().run_until_complete(main())