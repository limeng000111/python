'''
date:2020-01-10
'''
#水仙花数：一个三位数。个十百三位数的立方和等于这个数
#注意：Python3中除号用//，不是/
def cubic():
    x = int(input('请输入结尾的数'))
    for n in range(100,x):
        i = n//100
        j = n//10%10
        k = n%10
        if n == i + j**2 + k**3:
            print(n)
cubic()