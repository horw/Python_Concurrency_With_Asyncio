from threading import Lock, Thread
import time

lock_a = Lock()
lock_b = Lock()


def a():
    with lock_a:
        print('Acquired lock a from method a!')
        time.sleep(1)
        with lock_b:
            print('Acquired lock b from method b!')


def b():
    with lock_b:
        print('Acquired lock b from method b!')
        with lock_a:
            print('Acquired lock a from method b!')


thread_a = Thread(target=a,args=())
thread_b = Thread(target=b,args=())


thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()