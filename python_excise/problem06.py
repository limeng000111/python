'''
data:2020-01-13
'''
#有一组数列，2/1，3/2，5/3，8/5...求前20项之和.
from functools import reduce
def sequence():
    l = []
    a = 2
    b = 1
    s = 0
    for i in range(1,21):
        s += (a/b)
        l.append('%s/%s'%(a,b))
        a , b = a+b , a
    sum1 = reduce(lambda x,y:x+y,l)
    #print('数列的内容为：',l)
   # print('数列的前20项和:',sum1)
    print('+'.join(str(i) for i in l),end='\n')#学会使用.join的用法

    print('=%.2f'%s)
# sequence()

#递归当时求5i
# def fact(i):
# #     sum = 0
# #     if i == 0:
# #         sum = 1
# #     else:
# #         sum = i * fact(i-1)
# #     # print(sum)
# #     return sum
# # for j in range(5):
# #     print(j,fact(j))


def fact(i):
    sum = 0
    if i == 0:
        sum =1
    else:
        sum = i * fact(i-1)
    return sum#返回只是一个函数
    #print(sum)

#注意，递归函数需要调用才能生效
a = []
for j in range(5):
    a.append(fact(j))
print('n!的总和为%s'%reduce(lambda x,y:x+y,a))
