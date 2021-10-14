def pep8_warrior(class_name, bases, attrs):
    a = {}
    for name, val in attrs.items():
        if name.startswith('__'):
            a[name] = val
        elif isinstance(val, types.FunctionType):
            a[name.lower()] = val
        elif isinstance(val, type):
            buff = name.split('_')
            buff = [el.title() for el in buff]
            buff = ''.join(buff)
            a[buff] = val
        else:
            a[name.upper()] = val
    return type(class_name, bases, a)


class Pep8Warrior(type):
    def __new__(self, class_name, bases, attrs):
        a = {}
        for name, val in attrs.items():
            if name.startswith('__'):
                a[name] = val
            elif isinstance(val, types.FunctionType):
                a[name.lower()] = val
            elif isinstance(val, type):
                buff = name.split('_')
                buff = [el.title() for el in buff]
                buff = ''.join(buff)
                a[buff] = val
            else:
                a[name.upper()] = val
        return type(class_name, bases, a)


# class Dog(metaclass=PEp8Warrior):
#     class test_db:
#         test = 5
#
#     class kek:
#         test1 = 5
#
#     x = 5
#     y = 8
#
#     def heLLo(self):
#         print('Hi')
