import allure
import pytest

#
# @allure.feature('test_module_01')
# def test_case_01():
#     """
#     用例描述：Test case 01
#     """
#     assert 0
#
#
# @allure.feature('test_module_02')
# def test_case_02():
#     """
#     用例描述：Test case 02
#     """
#     assert 0 == 0
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', '-q', '--alluredir', './report/xml'])
# class Test_demo():
#     @pytest.mark.parametrize("a,b,excepted",[(1,3,5),(2,3,4),(3,6,9)])
#     def test_001(self,a,b,excepted):
#
#         assert a+b == excepted
#
#     @pytest.mark.parametrize("a,b,excepted",[(4,3,5),(2,3,4),(3,6,9)])
#     def test_002(self,a,b,excepted):
#         assert a-b == excepted
# @pytest.fixture()
# def test1():
#     a = 'leo'
#     b = '123456'
#     print('传出a,b')
#     return (a, b)
#
#
# def test2(test1):
#     u = test1[0]
#     p = test1[1]
#     assert u == 'leo'
#     assert p == '123456'
#     print('元祖形式正确')
#
#
# if __name__ == '__main__':
#     pytest.main('-q test_fixture.py')
# @pytest.fixture()
# def test1():
#     a = 'leo'
#     print('\n传出a')
#     return a
#
#
# @pytest.fixture(scope='function')
# def test2():
#     b = '男'
#     print('\n传出b')
#     return b
#
#
# def test3(test1):
#     name = 'leo'
#     print('找到name')
#     assert test1 == name
#
#
# def test4(test2):
#     sex = '男'
#     print('找到sex')
#     assert test2 == sex
#
#
# if __name__ == '__main__':
#     pytest.main('-q test_fixture.py')
@pytest.fixture()
def test1():
    a = 'leo'
    print('\n传出a')
    return a


@pytest.fixture(scope='function')
def test2():
    b = '男'
    print('\n传出b')
    return b


class TestCase:
    def test3(self, test1):
        name = 'leo'
        print('找到name')
        assert test1 == name

    def test4(self, test2):
        sex = '男'
        print('找到sex')
        assert test2 == sex


if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture.py'])