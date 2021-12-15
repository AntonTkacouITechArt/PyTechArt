import concurrent.futures
import threading
from threading import Thread

# def client(n: int | str) -> int|str:
from time import sleep


def client_2(semaphore):
    global i
    semaphore.acquire()
    print("Thread : " + threading.current_thread().getName())
    print("\nsleep\n")
    sleep(int(threading.current_thread().getName()) * 0.5)
    print("\nwake up\n")
    semaphore.release()


if __name__ == '__main__':
    semaphore = threading.Semaphore(value=3)
    for i in range(1, 10):
        t = Thread(target=client_2, args=(semaphore,), name=f"{i}")
        t.start()
