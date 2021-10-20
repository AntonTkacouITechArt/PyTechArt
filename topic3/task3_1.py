import re, typing
class RegParser:
    ADDRESS_REGEX = r'(?:^(?:[A-Z][a-z]*, )?(?:[A-Z][a-z]*(?: [Cc]ity)?, )?)[_\w\s-]+(?:, |str., )?(?:\d+\s*[-\/\\,|]\s*\d+)$'
    CONTACT_REGEX = r'^(?:(?P<age>age=[\d]+;?)|(?P<name>name=[\w\s-]+;?)|(?P<surname>surname=[\w\s-]+;?)|(?P<city>city=[\w\s-]+;?)){1,4}$'
    # PRICE_REGEX = r'(?:(?<=[$€] )(\d+(?:\.|,\d+)?\d*))|(?:(\d+(?:\.|,\d+)?\d*)(?=[ ]*BYN))'
    PRICE_REGEX = r'(?:(?<=[$€] )(?:\d+(?:\.|,\d+)?\d*))|(?:(?:\d+(?:\.|,\d+)?\d*)(?=[ ]*BYN))'
    # PRICE_REGEX = r'((?:(?<=[$€] )(\d+(?:(?:\.|\,)\d+)?\d*))|(?:(\d+(?:(?:\.|\,)\d+)?\d*)(?=[ ]*BYN)))'
    # PRICE_REGEX = r'((?:(?<=[$€] )(?:\d+(?:(?:\.|\,)\d+)?\d*))|(?:(?:\d+(?:(?:\.|\,)\d+)?\d*)(?=[ ]*BYN)))'
    @classmethod
    def find(cls, text: typing.Optional[str], choice: typing.Optional[int]):
        """Find address, contact, price"""
        data = None
        if choice == 1:
            data = re.findall(RegParser.ADDRESS_REGEX, text, re.MULTILINE)
        elif choice == 2:
            newdata = re.findall(RegParser.CONTACT_REGEX, text, re.MULTILINE)
            data = []
            for person in newdata:
                dict_per = {}
                for info in person:
                    if info != '':
                        el = info.replace(';', '').split('=')
                        dict_per.update({el[0]: el[1]})
                data.append(dict_per)
        elif choice == 3:
            groups_combinations = re.findall(RegParser.PRICE_REGEX, text,
                                             re.MULTILINE)
            print(groups_combinations)
            # x = [num.replace(',', '.') for group in groups_combinations
            #      for num in group if num != '']
            # print(x)
            # data = [
            #     int(num) if '.' not in num else float(num.replace(',', '.'))
            #     for num in x]
            data = [int(num) if ',' not in num and '.' not in num else float(num.replace(',','.'))  for num in groups_combinations ]
        return data

if __name__ == '__main__':
    # text1 = 'Belarus, Minsk city, Tolstoy str., 8 - 0303 Germany, Berlin City, Gauven, 23 - 1203'
    text1 = """Russia, Moscow City, Tolstoy- 123_456 str., 123 | 16
russia, Moscow City, Tolstoy str., 123 | 16
Russia, moscow City, Tolstoy str., 123 | 16
Russia, Moscow City, Tolstoy str., 123 | 16
Russia, Moscow City, Tolstoystr., 123 | 16
Russia, Moscow, Tolstoy, 123 , 16
Moscow, Tolstoy, 123-16
Moscow, Tolstoy, 123\16
 Moscow, Tolstoy, 123\16
Moscow, Tolstoy, 123\16"""
    text2 = 'name=Alex;age=20;city=Minsk city;surname=Larkin'
    # text3 = '$ 123, price = 12.123 BYN or € 6,03 and 3.14 BYN'
    text3 = """$ 123, price = 12.123 BYN or € 6,03 and 3.14"""
    text4 = """age=20;name=Alex;city=Minsk city
age=20;name=Alex;city=Minsk city;surname=Smith;age=22
age=22

surname=Smith;name=Alex;city=Minsk-city;age=20
surname=Smith,name=Alex,city=Minsk-city,age=20
 surname=Smith;name=Alex;city=Minsk-city;age=20"""
    text5="""$ 123, price = 12.123 BYN or € 6,03 and 3.14.
1321, $ 213. 21312 $ das 312,32
BYN 4242,32 $ 23.2 322, BYN 323,32 BYN
23. BYN 32, BYN   3232,23     BYN 
$  342,323 """
    print(RegParser.find(text5, 3))