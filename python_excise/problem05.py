'''
data:2020-01-12
'''
#一个小球从100米处落下，反弹至落下的一半，问：1/第10次落下后总共经历多少路程  2/第10次反弹多远
from functools import reduce
def ball(n):
    high = 100
    s = []#每次反弹高度的集合
    for i in range (0,n):
        res = high//2#反弹的高度
        high = high - res
        s.append(res)
    #总路程为反弹高度的3倍
    all_distance = reduce(lambda x,y:x+y,s) * 3
    #第n次反弹的距离
    print(s)
    distance = s[-1]
    print('总路程为：',all_distance)
    print('第%s次的反弹距离为：%s'%(n,distance))
#ball(10)
#print(ord('z'))


#两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比。请编程序找出三队赛手的名单
from itertools import permutations #这个函数是排序，返回值是一个iterators
def permutation():
    for i in permutations('xyz'):
        if i[0]!='x' and i[2]!='x' and i[2]!= 'y':
            print('a:%s,b:%s,c:%s'%(i[0],i[1],i[2]))
#permutation()

#用*打印菱形,分为上下两部分
from sys import stdout#找出sys与os的作用
def daimond():#菱形
    for i in range(4):
        for j in range(2-i+1):#公式需要留意
            stdout.write(' ')
        for k in range(2*i+1):
            stdout.write('*')
        print()

    for i in range(3):
        for j in range(i+1):
            stdout.write(' ')
        for k in range(4-2*i+1):
            stdout.write('*')
        print()
daimond()




