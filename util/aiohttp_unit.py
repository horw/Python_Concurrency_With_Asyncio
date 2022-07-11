import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url:str) -> int:
    async with(session.get(url)) as result:
        return result.status

async def another_fetch_status(session: ClientSession, url:str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with(session.get(url)) as result:
        return result.status


