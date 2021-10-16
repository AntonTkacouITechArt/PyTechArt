result = {}


def merge_students_data(csv_file: typing.Optional[typing.IO],
                        xlsx_workbook: typing.Optional[typing.IO],
                        json_file: typing.Optional[typing.IO],):
    data_from_csv = csv.reader(csv_file, delimiter=',')
    next(data_from_csv, None)
    result = {' '.join(row[0:2]): int(row[2]) for row in data_from_csv}
    data_from_xlsx = csv.reader(xlsx_workbook, delimiter=',',)
    for row in data_from_xlsx:
        print(row)
        name = ' '.join(row[0:1])
        nums = [int(num) for num in list(filter(None, row[1:-1]))]
        result[name] = {result[name]: nums}
    json.dump(result, json_file, indent=0)
