import concurrent.futures
import threading
from threading import Thread
from time import sleep


# def client(n: int | str) -> int|str:


def client(semaphore):
    semaphore.acquire()
    print(f"Thread : {threading.current_thread()}")
    print("sleep")
    sleep(2)
    print("wake up")
    semaphore.release()


if __name__ == '__main__':
    semaphore = threading.Semaphore(value=1)
    t1 = Thread(target=client, args=(semaphore,), name=f"thread {1}")
    t2 = Thread(target=client, args=(semaphore,), name=f"thread {2}")
    t3 = Thread(target=client, args=(semaphore,), name=f"thread {3}")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
