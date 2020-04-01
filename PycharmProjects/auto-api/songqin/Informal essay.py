import yaml
import os
import logging
import auto_api.log.log as log
import random
#获取当前目录
def write_yaml():
    base_dir = os.path.split(os.path.realpath(__file__))[0]

    logger = log.logger

    #yaml文件的路径
    base_file = base_dir +'\yaml.yaml'

    logger.info(base_file)

    #将数据写进yaml文件，读取文件用load,写入用dump
    json_data = {'name': '一条大河',
                 'age': 1956,
                 'job': ['Singer', 'Dancer']}

    # with open(base_file,'w') as fp:
    #     #y = yaml.dump(json_data,fp)
    #
    #     y = yaml.dump(json_data, default_flow_style=False).encode('utf-8').decode('unicode_escape')
    #     print(y)

    # with open(base_file,'w') as fp:
    #     yaml.dump(json_data,fp,default_flow_style=False,encoding='utf-8',allow_unicode=True)
    with open(base_file,'r') as fp:
        y = yaml.load_all(fp,Loader=yaml.Loader)
        for data in y :
            print(data)
implement = write_yaml()
dir = os.getcwd()
logging.info('-----------------dir----------------%s'%dir)
sep = os.sep
logging.info('-----------------sep----------------%s'%sep)

numList = [10,18,2,121,12,33,-11,1,-9,324,129]
def sort_num():
    for i in range(len(numList)-1):
        for j in range(len(numList)-1):
            if numList[j] > numList[j+1]:
                numList[j],numList[j+1] = numList[j+1],numList[j]
    print(numList)
a = sort_num()

def fn(x,n):
    s = 1
    while n>0:
        s = s * x
        n = n-1
    print(s)
b = fn(10,2)

def Sum_of_squares(*num):
    sum = 0
    for n in num:
        sum = sum + n*n
    print(sum)
c = Sum_of_squares(1,2,3,4,5,6,7,8,9,100)

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
d = fact(10)
print(d)

e = [d for d in os.listdir('.')]
print(e)

f = {'A':'a','B':'b'}
g = {y:x for x,y in f.items()}
print(g)

for i in range(1,10):
    for j in range(1,i+1):
        print('%d * %d = %d '%(j,i,i*j ),end='')
    print()


#随机生成6位验证码
list = []
for i in range(65,91):
    list.append(chr(i))
for k in range(97,123):
    list.append(chr(k))
for m in range(48,58):
    list.append(chr(m))
code = random.sample(list,6)
print(code)
print(type(code))
print('--------------')
code = ''.join(code)
print(code)


list1=[]
for i in range(65,91):
    list1.append(chr(i))     #通过for循环遍历asii追加到空列表中
for j in range(97,123):
    list1.append(chr(j))
for k in range(48,58):
    list1.append(chr(k))
ma = random.sample(list1,6)
print(ma)                    #获取到的为列表
ma = ''.join(ma)             #将列表转化为字符串
print(ma)
