import asyncpg
import asyncio

async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count = item_count + 1
        yield item


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='pgpwd4habr'
    )
    async with connection.transaction():
        query = "SELECT product_id, product_name FROM product"
        product_generator = connection.cursor(query)
        async for product in take(product_generator, 6):
            print(product)
        print('Got the first six products!')

    await connection.close()


asyncio.get_event_loop().run_until_complete(main())
