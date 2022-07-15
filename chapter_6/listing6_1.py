import time
from multiprocessing import Process


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time.time()
    print(f"Finished counting to {count_to} in {end-start}")
    return counter


def listing_():
    start_time = time.time()
    to_one_hungred_million = Process(target=count, args=(1000000000,))
    to_two_hungred_million = Process(target=count, args=(2000000000,))

    to_one_hungred_million.start()
    to_two_hungred_million.start()

    to_one_hungred_million.join()
    to_two_hungred_million.join()

    end_time = time.time()
    print(f"Completed in {end_time-start_time}")

