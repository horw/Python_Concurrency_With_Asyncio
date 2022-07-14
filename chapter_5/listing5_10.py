import asyncio
import logging
import asyncpg

async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='pgpwd4habr'
    )
    try:
        async with connection.transaction():
            insert_brand = "INSERT INTO brand VALUES(9999,'big brand')"
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)
    except Exception:
        logging.exception('Error while running transaction')
    finally:
        query = """
        SELECT brand_name FROM brand WHERE brand_name LIKE 'big%'"""
        brands = await connection.fetch(query)
        print(f'Query result was: {brands}')

        await connection.close()


asyncio.get_event_loop().run_until_complete(main())
