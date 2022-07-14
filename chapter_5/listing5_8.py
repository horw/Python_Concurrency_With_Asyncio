import asyncio
import asyncpg
from util import async_timed
from chapter_5.listing5_7 import product_query
from asyncpg import Pool


async def query_product(pool: Pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


@async_timed
async def query_products_synchronously(pool: Pool, queries):
    return [await query_product(pool) for _ in range(queries)]


@async_timed
async def query_product_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)

async def main():
    async with asyncpg.create_pool(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='pgpwd4habr',
        database='products',
        min_size=6,
        max_size=6
    ) as pool:
        await query_product_concurrently(pool,10000)
        await query_products_synchronously(pool,10000)

asyncio.get_event_loop().run_until_complete(main())
