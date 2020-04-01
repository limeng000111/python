'''
date:2019-12-17
author:limeng
'''
from operation_data import data_config
from tool import connect_db
from tool import operation_excel
from tool import operation_json
import json

class GetData():

    def __init__(self):
        self.oper_excel = operation_excel.OperationExcel()

    #获取excel测试用例的个数
    def get_case_lines(self):
        testcase_num = self.oper_excel.get_lines()
        return testcase_num

    #获取测试用例是否运行
    def get_run_case(self,row):
        flag = None
        col = int(data_config.get_is_run_value())
        run_model = self.oper_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #获取测试用例的id
    def get_case_id(self,row):
        col = int(data_config.get_id_value())
        id = self.oper_excel.get_cell_value(row,col)
        return id

    #获取测试用例的请求方式
    def get_method(self,row):
        col = int(data_config.get_request_type_value())
        method = self.oper_excel.get_cell_value(row,col)
        return method

    #获取测试用例的url
    def get_url(self,row):
        col = int(data_config.get_url_value())
        url = self.oper_excel.get_cell_value(row,col)
        return url

    #获取测试用例的请求数据
    def get_data(self,row):
        col = int(data_config.get_data_value())
        data = self.oper_excel.get_cell_value(row,col)
        # print(type(data))
        data = json.loads(data)
        # print(type(data))
        if data == '':
            pass
        # print(data)
        return data

    #获取测试用例的预期结果
    def get_except_result(self,row):
        col = int(data_config.get_except_result_value())
        data = self.oper_excel.get_cell_value(row,col)
        return data

    #向excel表格中写入测试结果
    def write_result(self,row,value):
        col = int(data_config.get_actually_result_value())
        self.oper_excel.write_value(row,col,value)


    def get_data_for_json(self, row):
        opera_json = operation_json.Operetionjson()
        request_data = opera_json.get_data('status')
        return request_data

if __name__ == '__main__':
     GetData().get_data(23)