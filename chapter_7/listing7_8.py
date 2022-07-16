import functools
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from util import async_timed

counter_lock = Lock()
counter: int = 0


def get_status_code(url: str) -> int:
    global counter
    responce = requests.get(url)
    with counter_lock:
        counter = counter + 1
    return responce.status_code


async def reporter(request_count: int):
    while counter < request_count:
        print(f'Finished {counter}/{request_count} requests')
        await asyncio.sleep(5)


@async_timed
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        requests_count = 1000
        urls = ['https://www.example.com' for _ in range(requests_count)]
        reporter_task = asyncio.create_task(reporter(requests_count))
        tasks = [loop.run_in_executor(
            pool,
            functools.partial(get_status_code, url)) for url in urls
        ]
        results = await asyncio.gather(*tasks)
        await reporter_task
        print(results)


asyncio.run(main())