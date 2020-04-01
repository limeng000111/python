import xlrd

class Handle_excel():

    def __init__(self,file = r'c:\users\dell\Desktop\auto_api.xlsx',sheet_id = 0):
        self.file = file
        self.sheet_id = sheet_id
        self.data = self.get_data()
    #获取某页sheet的名称
    def get_data(self):
        data = xlrd.open_workbook(r'c:\users\dell\Desktop\auto_api.xlsx')
        sheet = data.sheet_by_index(self.sheet_id)
        # print('---001---  %s '% sheet)
        return sheet
    #获取excel总行数
    def get_rows(self):
        rows = self.data.nrows
        # print('---002---  %s ' %  rows)
        return rows
    #获取某个单元格的具体数值（需要传入坐标）
    def get_cell(self,row,col):
        para1 = self.data.cell_value(row,col)
        # print('---003---  %s ' %  para1)
        return para1
    #通过url的坐标获取excel中的值
def get_url():
    url = 4
    return url
    #通过mothod的坐标获取excel中的值
def get_method():
    method = 5
    return method
    #通过paras的坐标获取excel中的值
def get_paras():
    paras = 8
    return paras

#通过expectValue的坐标获取excel中的值
def get_expectValue():
    expectValue = 9
    return expectValue

if __name__ == '__main__':
    t = Handle_excel()
    h1 = t.get_rows()
    h2 = t.get_data()
    h3 = t.get_cell(0,0)
