import pytest

# #定义全局函数
# def reverse(string):
#     return string[::-1]
#
# #测试用例(以test开头)
# def test__001():
#     string = 'limeng'
#     assert reverse(string)=="gn1emil
# def reverse(string):
#     return string[::-1]
#
# def test_reverse():
#     string = "good"
#     assert reverse(string) == "doog"
#
#     another_string = "itest"
#     assert reverse(another_string) == "sts11aeti"
#
# # if __name__=='__main__':
# #     pytest
def add_one(x,y):
    s = x+y
    return s
# def test_one():
#     assert add_one(1,2) == 3
#     assert add_one(1,3) == 3
def test_assert():
    with pytest.raises(ZeroDivisionError):
        1/0
