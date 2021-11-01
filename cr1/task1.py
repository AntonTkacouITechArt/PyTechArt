class Logger(type):
    def __new__(cls, class_name, bases, attrs):
        class LogItem(typing.NamedTuple):
            name: str
            args: list
            kwargs: dict
            result: typing.Optional[typing.Any]

        attrs.update(LogItem)

        def log(self):
            pass

        @property
        def last_log(self):
            return self.LogItem[-3:]

        return type(class_name, bases, attrs)
