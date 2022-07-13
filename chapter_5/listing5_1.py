import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='postgres',
                                       password='pgpwd4habr')
    version = connection.get_server_version()
    print(f'Connected! Postgres version is {version}')
    await connection.close()


asyncio.get_event_loop().run_until_complete(main())