import csv, typing, json

result = {}


def merge_students_data(csv_file, xlsx_workbook, json_file):
    with open(csv_file, newline='') as csv_file:
        data_from_csv = csv.reader(csv_file, delimiter=' ')
        print(data_from_csv)
        for row in data_from_csv:
            key = ' '.join(row[0:2])
            result[key] = {row[2]: []}
        print(result)
    with open(xlsx_workbook, newline='') as xlsx_file:
        data_from_xlsx = csv.reader(xlsx_file)
        print(data_from_xlsx)
        for row in data_from_xlsx:
          result[row[0]]=row[1:-1]
    print(result)

    with open(json_file, 'w+', ) as json_write:
        json.dump(result, json_write, indent=0)


merge_students_data('datacsv.csv', 'dataxlsx.xlsx', 'exmaple.json')
