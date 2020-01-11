'''
data:2020-01-11
'''
#一个数等于它所有的因子之和，称之为完数，找出2-1000中的这个数
from sys import stdout
'''
def find_numb(num):
     
    for i in range(1,num):
        k = []
        sum = 0
        for j in range(1,i):
            if i % j == 0:
                sum = sum + j
                k.append(j)
            if sum == i:
                print(i)

find_numb(100)
'''

#详细解法
a = 2
half = 0   #为此时计算数字的一半
Mylist = [] #保存不是素数的所有分解因子
flag = False   #判断是否有分解因子
sum = 0
while a <= 1000:
    half = a //2
    while half >= 1:
        if a % half == 0:
            Mylist.append(half)
            flag = True
        half = half -1
    if flag == True:
        for x in Mylist:
            sum += x
        if sum == a:
            print(a,'是完数')
            for y in Mylist:
                print(y,end=' ')#end是不要换行，间隔为一个空格
            print('\n')#\n代表换行
    a = a+1
    Mylist = []
    flag = False
    sum = 0

