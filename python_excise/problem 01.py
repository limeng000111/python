'''
time:2020-01-08
title:4位数字--1,2,3,4, 组成数字不重复的三位数，多少种解法
'''
def comb_sort():
    count = 0
    for i in range(1,5):
        for j in range(1,5):
            for n in range(1,5):
                if i != j and i != n and j !=n:
                    print(i,j,n)
                    count += 1
    print('总共有%s种排列方法'%count)
comb_sort()
#企业发放奖金根据利润提成，输入利润总额，算出利润值
def bouns(profits):
    if not isinstance(number,int):
        raise Exception("请输入数字")
    profits01 = 100000*0.1
    profits02 = profits01 + 100000*0.75
    profits03 = profits02 + 200000*0.05
    if profits <= 100000:
        num = 100000*0.1
    elif 100000<profits <= 200000:
        num = profits01 + (profits-100000)*0.075
    elif 200000 < profits <= 400000:
        num = profits02 +(profits-200000)*0.05
    elif 400000 < profits <= 600000:
        num = profits03 + (profits-400000)*0.03

    else:
        print('您输入的金额不符合')
    print('您的奖金为%s'%num)
number = int(input('请输入您的利润：'))
bouns(number)


