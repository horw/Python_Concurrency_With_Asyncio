import asyncio
from asyncio import StreamReader
from asyncio.subprocess import Process


async def write_output(prefix: str, stdout: StreamReader):
    while line := await stdout.readline():
        print(f'[{prefix}]: {line.rstrip()}')


async def main():
    program = ['cmd', '/c', 'dir']
    process: Process = await asyncio.create_subprocess_exec(*program,
                                                            stdout=asyncio.subprocess.PIPE)
    print(f'Process pid is: {process.pid}')
    stdout_task = asyncio.create_task(write_output(' '.join(program),
                                                   process.stdout))
    return_code, _ = await asyncio.gather(process.wait(), stdout_task)
    print(f'Process returned: {return_code}')


asyncio.get_event_loop().run_until_complete(main())
