import concurrent.futures
import threading
from threading import Thread, Semaphore
from time import sleep
import typing

# def client(n: int | str) -> int|str:


def client(semaphore: typing.Optional[threading.Semaphore]):
    semaphore.acquire()
    print(threading.current_thread().name)
    print("sleep")
    sleep(2)
    print("wake up")
    semaphore.release()


if __name__ == '__main__':
    semaphore = threading.Semaphore(value=1)
    threads = []
    for i in range(3):
        t = Thread(target=client, args=(semaphore,), name=f"thread {i}")
        threads.append(t)
        t.start()
    [thread.join() for thread in threads]
