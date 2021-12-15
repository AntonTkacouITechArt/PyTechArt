import threading
from threading import Thread
from time import sleep


def tourist():
    pass


def main():

    for i in range(1, 7):
        t = Thread(target=tourist, args=(), name=f"thread {i}")
    sleep(3)


if __name__ == '__main__':
    main()
