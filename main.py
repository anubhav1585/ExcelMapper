import openpyxl

def find_record(file_path):

    workbook = openpyxl.load_workbook(file_path)

    sheet = workbook.active

    rows = sheet.iter_rows(values_only=True)

    headers = next(rows)

    document_position = headers.index("Account No.")

    target = "CST0001009"

    for row in rows:

        current_value = row[document_position]

        if current_value == target:

            return row


result = find_record("source.xlsx")

print(result)
print(result[0])