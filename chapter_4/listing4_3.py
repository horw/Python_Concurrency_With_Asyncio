import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=1)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status


async def main():
    session_timeout = aiohttp.ClientTimeout(total=2, connect=1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session_timeout:
        await fetch_status(session_timeout, 'https://example.com')


asyncio.get_event_loop().run_until_complete(main())