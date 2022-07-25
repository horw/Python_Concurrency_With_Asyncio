import asyncio
from asyncio.subprocess import Process


async def main():
    program = ['cmd', 'python', 'chapter/listing13_9.py']
    process: Process = await asyncio.create_subprocess_exec(*program,
                                                            stdout=asyncio.subprocess.PIPE,
                                                            stdin=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate(b'zoot')
    print(stdout)
    print(stderr)


asyncio.get_event_loop().run_until_complete(main())