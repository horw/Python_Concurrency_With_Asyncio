import asyncio


@asyncio.coroutine
def coroutine():
    print('Sleeping')
    yield from asyncio.sleep(1)
    print('Finished')

asyncio.get_event_loop().run_until_complete(coroutine())