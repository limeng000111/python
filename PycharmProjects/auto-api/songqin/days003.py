import requests
import pytest


#当出现异常时，会抛出后面的异常（if status_code == 200....）
class Test_first():
    def test_baidu(self):
        r = requests.get('http://www.baidu.com')
        assert r.status_code == 100,('if status_code ==200,it is fault')

def leaf_year(year):
    if isinstance(year,int) is not True:
        raise TypeError('传入参数不是整数')
    elif year == 0:
        raise ValueError('传入数值不能为0')
    elif abs(year) != year:
        raise ValueError('传入的值不是正整数')
    elif (year % 4 == 0 and year %100 != 0) or year % 400 == 0:
        print('%s 是闰年' % year)
        return True
    else:
        print('%s 不是闰年' %year)
        return False
leaf_year(7)
