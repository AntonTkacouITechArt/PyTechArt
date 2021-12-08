import typing
import json
from openpyxl import load_workbook
result = {}


def merge_students_data(xlsx_workbook: typing.Optional[typing.IO],
                        json_file: typing.Optional[typing.IO], ):
    list1 = xlsx_workbook['Pi']
    last_row_key = ''
    for row in list1.rows:
        if row[0].value:
            last_row_key = row[0].value
            result[row[0].value] = {row[1].value: row[2].value}
        else:
            result[last_row_key].update({row[1].value: row[2].value})
    json.dump(result, json_file, indent=0)

if __name__ == '__main__':
    xlsx_workbook = load_workbook('empty_book.xlsx', )
    # csv_file = open('datacsv.csv', 'r')
    json_file = open('exmaple.json', 'w')
    merge_students_data(xlsx_workbook, json_file)
