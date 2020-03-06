import unittest
from Sherbet.test_method import RunMain
import json
import HTMLTestRunner
import time
import io

# class TestOne(unittest.TestCase):
#
#     def setUp(self):
#         self.run = RunMain
#
#
#
#     # def tearDownClass(self):
#     #     print('hello,I am teardown')
#
#     def test_001(self):
#         url = 'http://api.demobizpal.com/v_2_0_0/user/getUserInfo'
#         data = {'request_type':'android',
#                 'lang':'zh-cn',
#                 'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjbnNlbGxlcnMiLCJpYXQiOjE1NzIzMTM1MDYsImV4cCI6MTU3MjkxODMwNiwidXNlcl9pZCI6IjE1NjkzMTUwMjciLCJzaG9wX2lkIjoiMCJ9.dEjeZM95AYn2vLkdHDnxNrdFC4wSN52RdF6MZmVmWQ8',
#                 }
#         re = self.run.run_main(url,'GET',data)
#         print(re)
#         r = json.loads(re)
#
#         self.assertEqual(r['status'],'200','测试成功')
class TestMethod(unittest.TestCase):    # 定义一个类，继承自unittest.TestCase

    def setUp(self):
        url = 'http://api.demobizpal.com/v_2_0_0/user/getUserInfo'
        data = {'request_type': 'android',
                'lang': 'zh-cn',
                'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjbnNlbGxlcnMiLCJpYXQiOjE1NzIzMTM1MDYsImV4cCI6MTU3MjkxODMwNiwidXNlcl9pZCI6IjE1NjkzMTUwMjciLCJzaG9wX2lkIjoiMCJ9.dEjeZM95AYn2vLkdHDnxNrdFC4wSN52RdF6MZmVmWQ8',
                }
        self.run = RunMain(url,data)   # 在初始化方法中实例化get/post基类，生成一个实例对象，这样就不需要在每个用例中再进行实例化了


    def test_001(self):

        url = 'http://api.demobizpal.com/v_2_0_0/user/getUserInfo'
        data = {'request_type':'android',
                        'lang':'zh-cn',
                        'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjbnNlbGxlcnMiLCJpYXQiOjE1NzIzMTM1MDYsImV4cCI6MTU3MjkxODMwNiwidXNlcl9pZCI6IjE1NjkzMTUwMjciLCJzaG9wX2lkIjoiMCJ9.dEjeZM95AYn2vLkdHDnxNrdFC4wSN52RdF6MZmVmWQ8',
                        }
        r = self.run.run_main(url, 'POST', data)   # 调用RunMain类中run_main方法
        print(r)
        re = json.loads(r)
        print('status的类型%s'%type(re['status']))
        num = 200
        print('num 的类型：%s'%type(num))
        self.assertEqual(re['status'], num, '测试失败')
    def test_002(self):
        print('I am test_002')

    def tearDown(self) -> None:
        print('ok It is a new day')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    file = 'C:/Users/dell/PycharmProjects/auto-api/report/'+ now +'_testresult.html'
    fp = open(file,'wb')#创建测试报告文件

    suite = unittest.TestSuite()#创建测试套件
    suite.addTest(TestMethod('test_001'))#向测试套件中添加测试用例
    suite.addTest(TestMethod('test_002'))
    unittest.main()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title= '接口测试报告',description = '测试结果如下：')
    runner.run(suite)#执行测试
    fp.close()



