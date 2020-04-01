import random
from pathlib import Path

def creat_phone():
    #第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0,4)]

    #第三位数字
    third = {
        3 : random.randint(0,9),
        4 : [5,7,9][random.randint(0,2)],
        5 : [i for i in range(10) if i != 4 ][random.randint(0,8)],
        7 : [i for i in range(10) if i not  in [7,8,9]][random.randint(0,2)],
        8 : random.randint(0,9)
    }[second]

    #后8位数字
    suffix = random.randint(9999999,100000000)
    phone = '1{}{}{}'.format(second,third,suffix)
    #print(phone)
    return phone

#creat_phone()

path = r'C:\Users\dell\PycharmProjects\seautotest\lib\test.txt'
print(path)

def writetxt(phone):
    f = open(path,'a')
    f.write(phone + '\n')
    f.close()

def gettxt():
    try:
        f = open(path, 'r')
        sourceInLines = f.readlines()#按行读取内容
        return sourceInLines[0]
    except:
        pass
    f.close()
