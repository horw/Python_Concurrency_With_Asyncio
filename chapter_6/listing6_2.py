from multiprocessing import Pool


def say_hello(name:str) -> str:
    return f'Hi there, {name}'


def listing_():
    with Pool() as process_pool:
        hi_jeff = process_pool.apply(say_hello, args=('Jeff',))
        hi_john = process_pool.apply(say_hello, args=('John',))
        print(hi_jeff)
        print(hi_john)