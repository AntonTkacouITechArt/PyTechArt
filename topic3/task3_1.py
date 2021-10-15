import typing, re


class RegParser:
    ADDRESS_REGEX = '((?:[A-Z][a-z]*, )?(?:[A-Z][a-z]*(?: city| City)?, )?[_\w\s-]+(?:, | str., )?(?:\d+\s*[-/\\,|]\s*\d+))'
    # CONTACT_REGEX = '(age=[\w\s-]+;?)?(name=[\w\s-]+;?)?(surname=[\w\s-]+;?)?(city=[\w\s-]+;?)?'
    CONTACT_REGEX = '(name=[\w\s-]+;?)?(age=[\w\s-]+;?)?(city=[\w\s-]+;?)?(surname=[\w\s-]+;?)?'
    PRICE_REGEX = '(?:(?<=[$€] )(\d+(?:\.|,)?\d*))|(?:(\d+(?:\.|,)?\d*)(?=\s*BYN))'


    @classmethod
    def find(cls, text: typing.Optional[str], choice: typing.Optional[int]):
        data = None
        if choice == 1:
            exp = re.compile(RegParser.ADDRESS_REGEX)
            return exp.findall(text)
        elif choice == 2:
            # fixing empty string(None) and truble with regex
            exp = re.compile(RegParser.CONTACT_REGEX)
            print(exp.findall(text))
            a = exp.findall(text)

            return data
        elif choice == 3:
            # fixing empty string(None)
            exp = re.compile(RegParser.PRICE_REGEX)
            print(exp.findall(text))
            print(exp.group())
            return data
        else:
            print("Incorrect choice number! Try again!")

if __name__ == '__main__':
    text1 = 'Belarus, Minsk city, Tolstoy str., 8 - 0303 Germany, Berlin City, Gauven, 23 - 1203'
    text2 = 'name=Alex;age=20;city=Minsk city;surname=Larkin'
    text3 = '$ 5 $ 32,2 232,3232 BYN 2131 $ 232,2'
    text4 = 'age=20;city=Minsk city;surname=Larkin;name=Alex'

    RegParser.find(text4, 2)
