import openpyxl


def source_excel(source_file):
    # Load the source Excel file
    source_workbook = openpyxl.load_workbook(source_file)
    
    Source_sheet_list = source_workbook.sheetnames
    print("choose the sheet you want to copy from the source file:")
    for i in source_workbook.sheetnames:
        n = Source_sheet_list.index(i) + 1
        print(str(n) + ". " + i)

    source_sheet_choice = int(input("Enter the number of the sheet you want to copy: "))
    source_seleced_sheet = Source_sheet_list[source_sheet_choice - 1]

    source_sheet = source_workbook[source_seleced_sheet]

    rows = source_sheet.iter_rows(values_only=True)
    headers = next(rows) #it gives 1st row

    print("please give the unique Key:")
    for i in headers:
        print(i)

    unique_key = input("enter the Unique key:")


    unique_key_index = headers.index(unique_key) 

    for i in rows:
        print(i[unique_key_index])
        

    
  
  



source_excel("/Users/suresh/Desktop/App/ExcelMapper/source.xlsx")

    