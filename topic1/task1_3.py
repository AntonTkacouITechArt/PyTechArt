class FibIterator:
    def __init__(self):
        self.counter = 0
        self.limit = 100
        self.prev = 0
        self.next = 1

    def __next__(self):
        while self.counter < self.limit:
            yield self.prev
            self.prev, self.next = self.next, self.next + self.prev
            self.counter += 1

    def __iter__(self):
        self.counter = 0
        self.prev = 0
        self.next = 1
        return self


def fib_generator():
    prev = 0
    next = 1
    for _ in range(0, 100):
        yield prev
        buff = prev + next
        prev = next
        next = buff


def strange_decorator(func):
    def wrapper(*args, **kwargs):
        if (len(args) + len(kwargs)) > 10:
            raise ValueError
        if len(kwargs) != 0 and any(isinstance(v, bool) for v in kwargs.values()):
            raise TypeError
            # for k, v in kwargs.items():
            #     if isinstance(v, bool):
        a = func(*args, **kwargs)
        if isinstance(a, int):
            a += 13
        return a
    return wrapper
