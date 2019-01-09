import xlrd
book  = xlrd.open_workbook('gzb.xls')
print("the number of workshetts is {0}".format(book.nsheets))
print("worksheets name (s):{0}".format(book.sheet_names()))
sh =book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name,sh.nrows,sh.ncols))
print("cell D4 is {0}".format(sh.cell_value(rowx = 3,colx = 1)))
for l in range(sh.nrows):
    print(sh.row(l))
# xl.sheets()
# sheet = xl.sheets()[0]
# print(sheet)
# row = sheet.row_values(0)
# print(row)