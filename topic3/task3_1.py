class RegParser:
    ADDRESS_REGEX = r"""(?:^(?:[A-Z][a-z]*, )?(?:[A-Z][a-z]*(?: [Cc]ity)?, )?)[_\w\s-]+(?:, | str., )?(?:\d+\s*[-\/\\,|]\s*\d+)$"""
    CONTACT_REGEX = r"""^(?:(?:(?:age=(?P<age>[\d]+))(?:;)?)|(?:(?:(?:name=(?P<name>[\w\s-]+))(?:;)?))|(?:(?:surname=(?P<surname>[\w\s-]+))(?:;)?)|(?:(?:city=(?P<city>[\w\s-]+))(?:;)?)){1,4}$"""
    PRICE_REGEX = r"""(?:(?<=[$€] )(?:\d+(?:\.|,\d+)?\d*))|(?:(?:\d+(?:\.|,\d+)?\d*)(?=[ ]*BYN))"""

    @classmethod
    def find(cls, text: typing.Optional[str], choice: typing.Optional[int]):
        """Find address, contact, price"""
        regex = [
            lambda text: re.findall(RegParser.ADDRESS_REGEX, text,
                                    re.MULTILINE),
            lambda text: re.findall(RegParser.CONTACT_REGEX, text,
                                    re.MULTILINE),
            lambda text: re.findall(RegParser.PRICE_REGEX, text,
                                             re.MULTILINE)
        ]
        data = None
        newdata = regex[choice-1](text)
        if choice == 1:
            data = newdata
        elif choice == 2:
            data = [match.groupdict() for match in
                      re.finditer(RegParser.CONTACT_REGEX, text, re.MULTILINE)]
        elif choice == 3:
            data = [int(num) if ',' not in num and '.' not in num
                    else float(num.replace(',', '.'))
                    for num in newdata]
        return data
