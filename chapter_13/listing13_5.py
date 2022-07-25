import asyncio
from asyncio.subprocess import Process


async def main():
    program = ['cmd', 'python', 'listing13_5']
    process: Process = await asyncio.create_subprocess_exec(*program,
                                                            stdout=asyncio.subprocess.PIPE)
    print(f'Process pid is: {process.pid}')

    return_code = await process.wait()
    print(f'Process returned: {return_code}')


asyncio.get_event_loop().run_until_complete(main())