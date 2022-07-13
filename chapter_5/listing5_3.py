import asyncpg
import asyncio
from chapter_5.listing5_2 import *

async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='pgpwd4habr')

    statements = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        SIZE_INSERT,
        COLOR_INSERT
    ]

    print('Creating the product database...')
    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print('Finished creating the product database!')
    await connection.close()


asyncio.get_event_loop().run_until_complete(main())