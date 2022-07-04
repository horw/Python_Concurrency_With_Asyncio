import multiprocessing
import os


def hello_from_process():
    print(f'Hello from child process {os.getpid()}')


def list1_4():
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()

    print(f'Hello from parent process {os.getpid()}')

    hello_process.join()
