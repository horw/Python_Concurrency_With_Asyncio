from multiprocessing import Pool


def say_hello(name:str) -> str:
    return f'Hi there, {name}'


def listing_():
    with Pool() as process_pool:
        hi_jeff = process_pool.apply_async(say_hello,args=('Jeff',))
        hi_john = process_pool.apply_async(say_hello,args=('Jogn',))

        print(hi_jeff.get())
        print(hi_john.get())