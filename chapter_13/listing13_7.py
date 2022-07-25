import asyncio
import random
import string
import time
from asyncio.subprocess import Process


async def encrypt(text: str) -> bytes:
    program = ["C:\Program Files (x86)\GNU\GnuPG\gpg.exe", '-c', '--batch', '--passphrase', '3ncryptm3', '--cipher-algo',
               'TWOFISH']
    progress: Process = await asyncio.create_subprocess_exec(*program,
                                                             stdout=asyncio.subprocess.PIPE,
                                                             stdin=asyncio.subprocess.PIPE)
    stdout, stderr = await progress.communicate(text.encode())
    return stdout


async def main():
    text_list = [''.join(random.choice(string.ascii_letters) for _ in range(1000)) for _ in range(100)]
    s = time.time()
    tasks = [asyncio.create_task(encrypt(text)) for text in text_list]
    encrypted_text = await asyncio.gather(*tasks)
    e = time.time()

    print(f'Total time: {e-s}')
    print(encrypted_text)


asyncio.get_event_loop().run_until_complete(main())