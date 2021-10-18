import typing, re


class RegParser:
    ADDRESS_REGEX = '((?:[A-Z][a-z]*, )?(?:[A-Z][a-z]*(?: city| City)?, )?[_\w\s-]+(?:, | str., )?(?:\d+\s*[-/\\,|]\s*\d+))'
    CONTACT_REGEX = '(?P<age>age=[\w\s-]+;?)?(?P<name>name=[\w\s-]+;?)?(?P<surname>surname=[\w\s-]+;?)?(?P<city>city=[\w\s-]+;?)?'
    # CONTACT_REGEX = '(name=[\w\s-]+;?)?(age=[\w\s-]+;?)?(city=[\w\s-]+;?)?(surname=[\w\s-]+;?)?'
    PRICE_REGEX = '(?:(?<=[$€] )(\d+(?:\.|,)?\d*))|(?:(\d+(?:\.|,)?\d*)(?=\s*BYN))'

    @classmethod
    def find(cls, text: typing.Optional[str], choice: typing.Optional[int]):
        """Find address, contact, price"""
        data = None
        if choice == 1:
            data = re.findall(RegParser.ADDRESS_REGEX, text)
        elif choice == 2:
            # fixing empty string(None) and truble with regex
            data = exp.findall(RegParser.CONTACT_REGEX, text)
            print(data)
        elif choice == 3:
            groups_combinations = re.findall(RegParser.PRICE_REGEX, text)
            print(groups_combinations)
            x = [num.replace(',', '.') for group in groups_combinations
                 for num in group if num != '']
            data = [
                int(num) if '.' not in num else float(num.replace(',', '.'))
                for num in x]
        return data


if __name__ == '__main__':
    text1 = 'Belarus, Minsk city, Tolstoy str., 8 - 0303 Germany, Berlin City, Gauven, 23 - 1203'
    text2 = 'name=Alex;age=20;city=Minsk city;surname=Larkin'
    text3 = '$ 5 $ 32,2 232,3232 BYN 2131 $ 232,2'
    text4 = 'age=20;city=Minsk city;surname=Larkin;name=Alex'

    print(RegParser.find(text1, 1))
