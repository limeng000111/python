"""
@运行主函数
@2019-10-30
"""
from handle_excel import *
from test_method import *
import json
class Run_handle():
    def __init__(self):
        # url = 'http://api.demobizpal.com/v_2_0_0/user/getUserInfo'
        # data = {'request_type': 'android',
        #         'lang': 'zh-cn',
        #         'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjbnNlbGxlcnMiLCJpYXQiOjE1NzIzMTM1MDYsImV4cCI6MTU3MjkxODMwNiwidXNlcl9pZCI6IjE1NjkzMTUwMjciLCJzaG9wX2lkIjoiMCJ9.dEjeZM95AYn2vLkdHDnxNrdFC4wSN52RdF6MZmVmWQ8',
        #         }
        self.test_method = RunMain()
        self.handle_data = Handle_excel()

    def run_excel(self):
        nrow = self.handle_data.get_rows()
        print('---总行数---%s'%nrow)
        for i in range(1,nrow):
            print('程序00i%s即将运行'%i)
            #从excel中获取url
            url = self.handle_data.get_cell(i,get_url())
            # print('---url---:%s'%url)
            # print(type(url))
            # 从excel中获取method
            method = self.handle_data.get_cell(i,get_method())
            # print('---method---:%s'%method)
            # print(type(method))
            # 从excel中获取data
            data = json.loads(self.handle_data.get_cell(i,get_paras()))
            # print('---data---:%s'%data)
            # print(type(data))
            rel = self.test_method.run_main(url,method,data)
            # print(rel)
            expectValue = self.handle_data.get_cell(i,get_expectValue())
            # print('----expectValue的类型:%s---'%type(expectValue))
            if expectValue in rel:
                print('---测试通过---')
            else:
                print('---测试失败---')

if __name__ == '__main__':
    run = Run_handle()
    run.run_excel()
