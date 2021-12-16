# import threading
# import time
# from threading import Thread
# from time import sleep
#
#
# class SimpleEvent(threading.Event):
#     def __init__(self):
#         super().__init__()
#         self.start_time = time.time()
#
#     def delta_time(self) -> None:
#         end_time = time.time()
#         self.clear()
#         if int(end_time - self.start_time) in range(4, 6):
#             self.set()
#         elif int(end_time - self.start_time) > 10:
#             self.set()
#
#
# simple_event = SimpleEvent()
#
#
# def tourist():
#     while True:
#         simple_event.delta_time()
#         if simple_event.is_set():
#             print(threading.current_thread().name)
#             return 0
#
#
# def main():
#     for i in range(1, 10):
#         t = Thread(target=tourist, args=(), name=f"thread {i}\n")
#         t.start()
#         sleep(1)
#
#
# if __name__ == '__main__':
#     main()
#


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
    time.sleep(4)
    simple_event.set()
    time.sleep(2)
    simple_event.clear()
    time.sleep(4)
    simple_event.set()


def main():
    threads = []
    for i in range(1, 7):
        t = Thread(target=tourist, args=(i,), name=f"thread {i}")
        threads.append(t)
        t.start()
    sleep(3)
    thread_border_guard = Thread(target=border_guard)
    threads.append(thread_border_guard)
    thread_border_guard.start()
    join_thread = lambda x: x.join()
    [join_thread(thread) for thread in threads]


if __name__ == '__main__':
    main()
