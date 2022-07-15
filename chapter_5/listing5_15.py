import asyncpg
import asyncio


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='pgpwd4habr'
    )
    query = "SELECT product_id, product_name FROM product"
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)
    await connection.close()


asyncio.get_event_loop().run_until_complete(main())