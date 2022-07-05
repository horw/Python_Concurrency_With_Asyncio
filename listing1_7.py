import time
import requests


def real_example() -> None:
    response = requests.get('https://example.com')
    print(response.status_code)


sync_start = time.time()

real_example()
real_example()

sync_end = time.time()

print(f'Running synchronously took {sync_start - sync_end:.4f} seconds.')
