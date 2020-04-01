#utlis:封装工具类
#-*-coding : utf-8 -*-
import xlrd
import xlsxwriter
import json
from pathlib import Path

class Excel():
    def __init__(self,type,file_name):
        if type == 'r':  #文本的状态支持可读
            #打开表格
            self.workbook = xlrd.open_workbook(file_name)
            #获取每页的名称
            self.sheet_names = self.workbook.sheet_names()
            #新建一个列表，将每行的测试用例数据提取出来保存
            self.list_data = []
        elif type == 'w':
            self.workbook = xlsxwriter.Workbook(file_name)

    def read(self):
        #获取每页的名称
        for sheet_name in self.sheet_names:
            #获取每页的内容
            sheet = self.workbook.sheet_by_name(sheet_name)
            #获取总行数
            nrow = sheet.nrows
            for i in range(0,nrow):
                #获取每行的值
                rowvalue = sheet.row_values(i)
                #将每行数据加入列表
                self.list_data.append(rowvalue)
        return self.list_data

def elements_tojson(element):
        #将数据处理成json
        #定义一个字典
    elements = {}
    for i in element:
        elements[i[2]] = {'type':i[4],'data':i[5]}
    #return elements
    print(elements)

def datatodict(data):
    header = {
        'id' : "id",
        '模块' : "model",
        '描述' : "desc",
        'url' :"url",
        '请求类型' : "resquest_type",
        'data数据' : "paras",
        '预期结果' : "except_res",
        '实际结果' : "real_res",
        '是否运行' : "is_run"

    }
    head = []
    list_dict_data = []
    for i in data[0]:
        #将标题中对应的英文放在列表中get(i,i):取i对应的值，如果没有取到，则展示原值
        head.append(header.get(i,i))

    for d in data[1:]:
    #将数据组合成json
        data_dict = {}
        for n in range(len(head)):
            if isinstance(d[n],str):
                data_dict[head[n]] = d[n].strip()
            else:
                data_dict[head[n]] = d[n]
        list_dict_data.append(data_dict)
        return list_dict_data
        #print(list_dict_data)

#dict格式的数据处理为测试套间格式
def suite_format(data):
    #用例套件list
    testsuite = []
    #每个用例的testcase
    testcase = {}

    #for循环得到所有数据
    for d in data:
        if d['id'].strip():
            #判断是否存在，存在则继续运行
            if testcase:
                testsuite.append(testcase)
                #将testcase置空
                testcase = {}
            for key in ("id", "model","desc","url","resquest_type","paras","except_res","real_res","is_run"):
                testcase[key] = d[key]


                testsuite.append(testcase)

    #print(testsuite)
    return testsuite

#判断是否存在文件,不存在则创建
def mkdir(p):
    path = Path(p)
    if not path.is_dir():
        path.mkdir()




if __name__ == '__main__':
    filename = 'c:\\Users\\dell\\Desktop\\testcase.xls'
    e = Excel('r',filename)
    #读取返回的内容
    list_read = e.read()
  #  print(list_read[0])
    #elements_tojson(list_read)
    data = datatodict(list_read)
    testsuit = suite_format(data)
    print(testsuit)
    #



