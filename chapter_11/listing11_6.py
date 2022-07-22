import asyncio
from asyncio import Semaphore


async def operation(semaphore: Semaphore):
    print('Waiting to acquire semaphore...')
    async with semaphore:
        print('Semaphore acquired!')
        await asyncio.sleep(2)
    print('Semaphore released!')


async def main():
    semaphore = Semaphore(2)
    await asyncio.gather(*[operation(semaphore) for _ in range(5)])


asyncio.get_event_loop().run_until_complete(main())