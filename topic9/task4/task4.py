import threading
import time
from threading import Thread
from time import sleep


class SimpleEvent(threading.Event):
    def __init__(self):
        super().__init__()
        self.start_time = time.time()

    def delta_time(self) -> None:
        end_time = time.time()
        self.clear()
        if int(end_time - self.start_time) in range(4, 6):
            self.set()
        elif int(end_time - self.start_time) > 10:
            self.set()


simple_event = SimpleEvent()


def tourist():
    while True:
        simple_event.delta_time()
        if simple_event.is_set():
            print(threading.current_thread().name)
            return 0


def main():
    for i in range(1, 10):
        t = Thread(target=tourist, args=(), name=f"thread {i}\n")
        t.start()
        sleep(1)


if __name__ == '__main__':
    main()
