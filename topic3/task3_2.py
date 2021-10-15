result = {}

#i dont know why
def merge_students_data(csv_file: typing.Optional[file],
                        xlsx_workbook: typing.Optional[file],
                        json_file: typing.Optional[file]) -> typing.Dict[
                        str, typing.Dict[int, typing.List[int]]]:
    data_from_csv = csv.reader(csv_file)
    for row in data_from_csv:
        key = ' '.join(row[0:2])
        result[key] = row[2]

    data_from_xlsx = csv.reader(xlsx_workbook, delimiter=' ',)
    for i, row in enumerate(data_from_xlsx):
        row = list(filter(None, row))
        result[row[0]] = {result[row[0]]: row[1:-1]}

    json.dump(result, json_file, indent=0)

# merge_students_data('datacsv.csv', 'dataxlsx.xlsx', 'exmaple.json')
