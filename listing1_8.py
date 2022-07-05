import time
import threading
import requests


def real_example() -> None:
    response = requests.get('https://example.com')
    print(response.status_code)

thread_1 = threading.Thread(target=real_example)
thread_2 = threading.Thread(target=real_example)

thread_start = time.time()

thread_1.start()
thread_2.start()

print('all thread running!')

thread_1.join()
thread_2.join()

thread_end=time.time()

print(f'Running with threads took {thread_end - thread_start:.4f} seconds.')
