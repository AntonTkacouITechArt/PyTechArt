import threading
import time
from threading import Thread
from time import sleep

"""Need to debug really, condition is like lamp??"""


simple_event = threading.Event()
simple_condition = threading.Condition()


def tourist(n):
    simple_event.set()
    with simple_condition:
        print(n)
    simple_event.clear()

def border_guard():
    simple_event.set()

    for _ in range(3):
        simple_condition.notify()
        time.sleep(1)

    simple_condition.notify_all()

def main():
    threads = []
    for i in range(1, 7):
        t = Thread(target=tourist, args=(i,), name=f"thread {i}")
        t.start()
        threads.append(t)
    sleep(3)
    thread_border_guard = Thread(target=border_guard)
    thread_border_guard.start()
    threads.append(thread_border_guard)
    join_thread = lambda x: x.join()
    [join_thread(thread) for thread in threads]


if __name__ == '__main__':
    main()
