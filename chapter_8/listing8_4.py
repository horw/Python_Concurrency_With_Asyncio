import asyncio
from util import delay
from chapter_8.listing8_5 import create_stdin_reader


async def main():
    stdin_reader = await create_stdin_reader()
    while True:
        # delay_time = input('Enter a time to sleep:')
        # asyncio.create_task(delay(int(delay_time)))
        # await asyncio.sleep(0)
        delay_time = await stdin_reader.readline()
        asyncio.create_task(delay(int(delay_time)))


asyncio.run(main())
