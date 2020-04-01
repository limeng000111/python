import xlrd
#‪c:\Users\dell\Desktop\auto_api.xlsx
filename = r'c:\users\dell\Desktop\auto_api.xlsx'
#打开接口测试用例
data = xlrd.open_workbook(filename)

sheets = data.sheet_names()
print(sheets)
print(sheets[0])
#选中第一个excel
sheet1 = data.sheet_by_index(0)
#获取sheet1的总行数
rows = sheet1.nrows
print('excel的总行数：%s'%rows)
#获取总列数
cols = sheet1.ncols
print('excel的总列数:%s'%cols)
#获取第3列的数据
col_data = sheet1.col_values(2)
print('第3列的数据%s'%col_data)
#通过坐标获取对应位置的数据
data001 = sheet1.cell_value(1,4)
print(data001)