import unittest
from model import HTMLTestRunner
def all_case():
    #执行测试用例的目录
    casedir = r'C:\Users\dell\PycharmProjects\selenium_auto\test_case'
    #生成测试套件
    testcase = unittest.TestSuite()
    #通过discover找出筛选出的测试用例
    discover = unittest.defaultTestLoader.discover(casedir,pattern='test*.py')
    #讲discover筛选出来的测试用例添加到测试套件中
    for test_suit in discover:
        for test_case in test_suit:
            #将测试用例添加到测试套件中
            testcase.addTest(test_case)
    return testcase

if __name__ == '__main__':
    #生成报告的路径
    report_file = r'C:\Users\dell\PycharmProjects\selenium_auto\report\result.html'
    # with open(report_file,'wb') as f:
    f = open(report_file,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title = '畅销天下测试报告',description='详细信息请见下图')
        #run所有的测试用例
    runner.run(all_case())

    f.close()