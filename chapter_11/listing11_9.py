import asyncio
from asyncio import BoundedSemaphore


async def main():
    semaphore = BoundedSemaphore(1)

    await semaphore.acquire()
    semaphore.release()
    semaphore.release()


asyncio.get_event_loop().run_until_complete(main())