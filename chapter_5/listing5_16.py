import asyncio
import asyncpg



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
        cursor = await connection.cursor(query)
        await cursor.forward(500)
        products = await cursor.fetch(100)
        for product in products:
            print(product)

    await connection.close()

asyncio.get_event_loop().run_until_complete(main())