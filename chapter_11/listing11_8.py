import asyncio
from asyncio import Semaphore


async def acquire(semaphore: Semaphore):
    print('Waiting to acquire')
    async with semaphore:
        print('Aquired')
        await asyncio.sleep(5)
    print('Releasing')


async def release(semaphore: Semaphore):
    print('Releasing as a one off!')
    semaphore.release()
    print('Released as a one off!')


async def main():
    semaphore = Semaphore(2)

    print("Acquiring twice, releasing three times...")
    await asyncio.gather(
        acquire(semaphore),
        acquire(semaphore),
        release(semaphore)
    )
    print('Acquiring three times...')
    await asyncio.gather(
        acquire(semaphore),
        acquire(semaphore),
        acquire(semaphore),
    )

asyncio.get_event_loop().run_until_complete(main())