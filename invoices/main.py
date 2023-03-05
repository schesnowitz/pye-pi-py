import pandas as pd
import openpyxl
import glob




sheets = glob.glob('sheets/*.xlsx')
# print(sheets)

for sheet in sheets:
    df = pd.read_excel(sheet, sheet_name='Sheet 1')
    print(df)