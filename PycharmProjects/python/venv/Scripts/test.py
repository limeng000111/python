import pytest

@pytest.mark.parametrize('mycase',case.list,ids=case.name)#装饰器
pytest.skip('skip testcase:(%s)'%mycase['name'])#跳过测试用例
pytest.xfail("previous test fild(%s)"%mycase['name'])#跳过会失败的测试用例
pytest -m pytest -s -q --alluredir ./report#控制台输出每一步结果
