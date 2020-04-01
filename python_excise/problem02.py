'''
time:2020-01-09
一个数，加上100是一个完全平方数，加上268又是一个完全平方数，求这个数
'''
import math

for i in range(100001):
    x = int(math.sqrt(i + 100))
    j = int(math.sqrt(i + 368))
    if (x*x == i+100) and (j*j == i+368):
        print(i)
        print(x,j)
        print(x*x,j*j)

#problem02:输入某年某日某天，输出这是第几天
year = int(input('请输入年份'))
month = int(input('请输入月份'))
day = int(input('请输入天数'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 1<= month <= 12:
    sum = months[month-1]
else:
    print('input month is error')
sum = sum + day

leap = 0
if (year%400 == 0) or (year%4==0) and(year%100!=0):
    leap = 1
if (leap == 1) and (month>2):
    sum = sum+1
print('总天数为%s'%sum)
