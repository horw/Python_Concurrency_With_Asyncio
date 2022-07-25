import asyncio
from asyncio.subprocess import Process


async def main():
    program = [ 'python', 'chapter_13/listing13_4.py']
    process: Process = await asyncio.create_subprocess_exec(*program,
                                                            stdout=asyncio.subprocess.PIPE)
    print(f'Process pid is: {process.pid}')
    stdout, stderr =await process.communicate()
    print(stdout)
    print(stderr)

    print(f'Process returned: {process.returncode}')


asyncio.get_event_loop().run_until_complete(main())