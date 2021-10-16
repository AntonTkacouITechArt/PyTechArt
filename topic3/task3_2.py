result = {}


def merge_students_data(csv_file: typing.Optional[typing.IO],
                        xlsx_workbook: typing.Optional[typing.IO],
                        json_file: typing.Optional[typing.IO]):
    data_from_csv = csv.reader(csv_file,delimiter=' ')
    result = {' '.join(row[0:2]):int(row[2]) for row in data_from_csv}
    data_from_xlsx = csv.reader(xlsx_workbook, delimiter=',',)
    for row in data_from_xlsx:
        name = row[0]
        nums = [int(num) for num in list(filter(None, row[1:-1]))]
        result[row[0]] = {result[name]: nums}
    json.dump(result, json_file, indent=0)

