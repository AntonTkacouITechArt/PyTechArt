import collections, typing, fractions, decimal
min_max_tuple = collections.namedtuple('min_max_tuple',
                                       ['max_value', 'min_value'])
def get_max_and_min(data: typing.Set[typing.Union[decimal.Decimal,
                fractions.Fraction, str]]) -> collections.namedtuple:
    """Get a set of float(ex: 231.2312) and str data("1 \ 5" or "3.00000003") ->
     return namedtuple with attribute .max_value and .min_value """
    buff = list()
    for el in data:
        if isinstance(el, float):
            buff.append(el)
        else:
            if '\\' in el:
                buff.append(fractions.Fraction(el.replace('\\', '/').replace(' ', '')))
            elif '.' in el:
                buff.append(decimal.Decimal(el))
    return min_max_tuple(max(buff), min(buff))

if __name__ == '__main__':
    data = {
        1.21312,
        32.231,
        23.41,
        1.0,
        "1 \\ 5",
        "20.13",
        "23.231",
        "100.00",
        "131.123",
    }
    test = get_max_and_min(data)
    print(test.min_value)
    print(test.max_value)
