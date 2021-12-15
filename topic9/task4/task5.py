import threading
from threading import Thread
from time import sleep

barrier = threading.Barrier(5)


def roller_coaster():
    print(f'Thread {threading.current_thread().name} в ожидании барьера с {barrier.n_waiting} другими')
    try:
        barrier.wait(timeout=4)
    except threading.BrokenBarrierError:
        barrier.reset()
    print(threading.currentThread().getName)



if __name__ == '__main__':
    threads = []
    for i in range(1, 36):
        t = Thread(target=roller_coaster, name=f"thread: {i}")
        threads.append(t)
        t.start()
        if i in range(1, 21):
            sleep(0.5)
        elif i in range(21, 31):
            sleep(1)
        else:
            sleep(2)
    [thread.join() for thread in threads]
