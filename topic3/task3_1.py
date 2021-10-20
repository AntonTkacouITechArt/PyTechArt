class RegParser:
    ADDRESS_REGEX = r"""(?:^(?:[A-Z][a-z]*, )?(?:[A-Z][a-z]*(?: [Cc]ity)?, )?)[_\w\s-]+(?:, | str., )?(?:\d+\s*[-\/\\,|]\s*\d+)$"""
    CONTACT_REGEX = r"""^(?:(?:(?:age=(?P<age>[\d]+))(?:;)?)|(?:(?:(?:name=(?P<name>[\w\s-]+))(?:;)?))|(?:(?:surname=(?P<surname>[\w\s-]+))(?:;)?)|(?:(?:city=(?P<city>[\w\s-]+))(?:;)?)){1,4}$"""
    PRICE_REGEX = r"""(?:(?<=[$€] )(?:\d+(?:\.|,\d+)?\d*))|(?:(?:\d+(?:\.|,\d+)?\d*)(?=[ ]*BYN))"""

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
                for i, info in enumerate(person):
                    if info != '':
                        if i == 0:
                            dict_per.update({'age': info})
                        elif i == 1:
                            dict_per.update({'name': info})
                        elif i == 2:
                            dict_per.update({'surname': info})
                        elif i == 3:
                            dict_per.update({'city': info})
                data.append(dict_per)
        elif choice == 3:
            groups_combinations = re.findall(RegParser.PRICE_REGEX, text,
                                             re.MULTILINE)
            data = [int(num) if ',' not in num and '.' not in num
                    else float(num.replace(',', '.'))
                    for num in groups_combinations]
        return data

if __name__ == '__main__':
     xlsx_workbook = load_workbook('empty_book.xlsx', )
     csv_file = open('datacsv.csv', 'r')
     json_file = open('exmaple.json', 'w')
     merge_students_data(csv_file, xlsx_workbook, json_file)