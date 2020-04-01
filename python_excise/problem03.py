'''
date:2020-01-10
'''
#水仙花数：一个三位数。个十百三位数的立方和等于这个数
#注意：Python3中除号用//，不是/
def cubic():
    x = int(input('请输入计算的数'))
    if not 100<=x<1000:
        raise Exception('输入的数值需要是三位数')
    for n in range(100,x):
        i = n//100
        j = n//10%10
        k = n%10
        if n == i + j**2 + k**3:
            print(n)
# cubic()

#分解一个数的正整数质因数
def decomposition():
    num = int(input("请输入需要分解的正整数:"))
    if num <= 0:
        raise Exception('数值需要大于0')
    prime = int(2)
    res = []
    while prime<=num:
        if num % prime ==0:
            res.append(prime)
            num = num//prime
        else:
            prime = prime +1
    print(res)
# decomposition()

# n=int(input("请输入正整数："))
# prime=int(2)
# if n==prime:
#     print(n)
# else:
#     while (n>=prime):
#         k=n%prime
#         if( k == 0):
#             print(prime)
#             n=n/prime
#         else:
#             prime=prime+1

#输入一串字符，统计字母，数字，空格，其他的个数
def count():
    cha = str(input('请输入需要统计的字符串:'))
    shuzi = 0
    zimu = 0
    kongge = 0
    qita = 0
    for one in cha:
        if one.isdigit():
            shuzi += 1
        if one.isalpha():
            shuzi += 1
        if one.isspace():
            kongge += 1
        else:
            qita += 1
    print(shuzi,zimu,kongge,qita)
    return shuzi,zimu,kongge,qita
# count()

#求s = a+aa+aaa+aaaa的和，几个和是几均由变量控制
from functools import reduce
def Sum_count():
    Tn=0   #累计后的当前值
    Sn=[]  #列表中的值
    n = int(input('数字的长度'))
    a = int(input('需要统计的数字'))
    for d in range(n):
        Tn = Tn + a
        a = a*10
        print('当前的值为：%s'%Tn)
        Sn.append(Tn)
    Sum = reduce(lambda x,y:x+y,Sn)
    print('统计的总和为：%s'%Sum)
Sum_count()





