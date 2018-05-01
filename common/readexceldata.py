import xlrd

data = xlrd.open_workbook("testdata.xlsx")
table = data.sheet_by_name("Sheet1")

nrows = table.nrows
ncols = table.ncols
print(nrows)
print(ncols)

print(table.row_values(0))
print(table.col_values(0))
