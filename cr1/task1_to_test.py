class Logger(type):
    def __new__(cls, clsname, bases, attrs):
        class LogItem(typing.NamedTuple):
            name: str
            args: list
            kwargs: dict
            result: typing.Any

        def log(self):
            pass

        @property
        def last_log(self):
            return self.LogItem[-3:]

        newclass = super(Logger, cls).__new__(cls, clsname, bases, attrs)
        setattr(newclass, log.__name__, log)
        setattr(newclass, LogItem.__name__, LogItem)
        setattr(newclass, last_log.__name__, last_log)
        return newclass