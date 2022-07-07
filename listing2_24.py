import asyncio
from util import delay


async def main():
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = .250


asyncio.run(main(), debug=True)