import re, typing


class RegParser:
    ADDRESS_REGEX = '([A-Z][a-z]*, )?([A-Z][a-z]*( city| City)?, )?[_\w\s-]+(, | str., )?(\d+\s*[-/\\,|]\s*\d+)'
    CONTACT_REGEX = '(age=[\w\s-]+;?)?(name=[\w\s-]+;?)?(surname=[\w\s-]+;?)?(city=[\w\s-]+;?)?'
    PRICE_REGEX = '(?:(?!^[$€] )(\d+(?:.|,)?\d*))|(?:(\d+(?:.|,)?\d*)(?=\s*BYN$))'

    @classmethod
    def find(cls, text: typing.Optional[str], choice: typing.Optional[int]):
        if choice == 1:
            exp = re.compile(RegParser.ADDRESS_REGEX)
            print(exp.findall(text))
            print(exp.match(text).group())
        elif choice == 2:
            pass
        elif choice == 3:
            exp = re.compile(RegParser.PRICE_REGEX)
            print(exp.match(text))
            print(exp.match(text).group())
            print(exp.findall(text))
            print(exp.match(text).group())
        else:
            print("Incorrect choice number! Try again!")


if __name__ == '__main__':
    text1 = 'Belarus, Minsk city, Tolstoy str., 8 - 0303 Germany, Berlin City, Gauven, 23 - 1203'
    text2 = 'name=Alex;age=20;city=Minsk city;surname=Larkin'
    text3 = '13.28 BYN $ 5 $ 36 2312,231 BYN'

    RegParser.find(text3, 3)
