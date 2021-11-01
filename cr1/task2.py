result = {}


def xlsx_to_json(xlsx_workbook: typing.Optional[typing.IO],
                 json_file: typing.Optional[typing.IO], ):
    list1 = xlsx_workbook['List']
    last_row_key = ''
    for row in list1.rows:
        if row[0].value:
            last_row_key = row[0].value
            result[row[0].value] = {row[1].value: row[2].value}
        else:
            result[last_row_key].update({row[1].value: row[2].value})
    json.dump(result, json_file, indent=0)
