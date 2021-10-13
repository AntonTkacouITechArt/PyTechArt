import types


def pep8_warrior():
    pass


# how to use types, dont know really
class PEp8Warrior(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}
        for name, val in attrs.items():
            if name.startswith('__'):
                a[name] = val
            elif isinstance(val, types.FunctionType):
                a[name.lower()] = val
            elif type(val) == type:
                a[]
            else:
                a[name.upper()] = val
        return a


class D:
    test = 5

class Dog(metaclass=PEp8Warrior):
    x = 5
    y = 8

    def heLLo(self):
        print('Hi')

print(Dog)
