import asyncio
from util import delay
from chapter_8.listing8_5 import create_stdin_reader
import sys

async def main():


    #stdin_reader = await create_stdin_reader()
    loop =  asyncio.get_running_loop()
    while True:

        # delay_time = input('Enter a time to sleep:')
        # asyncio.create_task(delay(int(delay_time)))
        # await asyncio.sleep(0)


        asyncio.create_task(delay(int(delay_time)))


asyncio.new_event_loop().run_until_complete(main())
