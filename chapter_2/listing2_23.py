import asyncio
from util import delay,async_timed


@async_timed
async def cpu_bound_work() -> int:
    count = 0
    for i in range(100000000):
        count = count + 1
    return count

async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one

asyncio.run(main(), debug=True)