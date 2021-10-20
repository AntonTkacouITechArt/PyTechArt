result = {}


def merge_students_data(csv_file: typing.Optional[typing.IO],
                        xlsx_workbook: typing.Optional[typing.IO],
                        json_file: typing.Optional[typing.IO], ):
    data_from_csv = csv.reader(csv_file, delimiter=',')
    next(data_from_csv, None)
    result = {' '.join(row[0:2]): int(row[2]) for row in data_from_csv}
    # replace List1 =>  Pi to debug
    list1 = xlsx_workbook['List1']
    # list1 = xlsx_workbook['List1']
    for i, row in enumerate(list1.rows):
        if i != 0:
            result[row[0].value] = {'age': result[row[0].value], 'marks': []}
            for col in row[1:-1]:
                if col.value is not None:
                    result[row[0].value]['marks'].append(col.value)
    json.dump(result, json_file, indent=0)

 if __name__ == '__main__':
     xlsx_workbook = load_workbook('empty_book.xlsx', )
     csv_file = open('datacsv.csv', 'r')
     json_file = open('exmaple.json', 'w')
     merge_students_data(csv_file, xlsx_workbook, json_file)