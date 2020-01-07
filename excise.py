#快速排列
def quick_sort(list001,right,left):
    # 设置退出条件，注意：不是退出循环，是判断List不能只有一个数，否则无意义
    if right >= left:
        return
    low = right
    hight = left
    #设置初始的中间值
    mid = list001[right]

    while low < hight:
        #进入循环，开始比较
        while low < hight and list001[hight] >= mid :
            hight -= 1
        #如果左边的值不大于中间值，调到最右边
        list001[low] = list001[hight]
        #开始从右往左排序
        while low < hight and list001[low] < mid:
            low += 1
        #如果左边的值大于中间值，则调到右边
        list001[hight] = list001[low]
    #推出循环，此时low和hight重合
    #赋予最新的中间值
    list001[low] = mid
    #递归进行排序
    #对左边的值进行排序
    quick_sort(list001,right,low - 1)
    #对右边的值进行排序
    quick_sort(list001,low + 1,left)
import random
list001 = []
for i in range(6):
    a = random.randint(0,101)
    list001.append(a)
print('排序前的序列%s'%list001)
quick_sort(list001,0,len(list001)-1)
print('排序后的序列%s'%list001)

#冒泡排序
def bubbling_sort(a):
    #设置一个冒泡排序的标志为Flase
    ex_flag = False
    for i in range(len(a)-1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                ex_flag = True
        if  not ex_flag:
            print(a)
    print(a)
a = [12,32,34,3,45,3]
bubbling_sort(a)

# 算数组中查找出现次数过半的数
b = [12,34,1,33,3,3,33,33,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,123,2,2,2,2,2,2,2,2,2,2,2,2,11]
num = []
res = 0
for i in b:
    if i not in num:
        num.append(i)
    else:
        res = b.count(i)
        mid = len(b)//2
        if res >= mid:
             print(i)
             break

def FindMoreHalf(d):
    longth = len(d)
    if longth <= 1:
        return 1
    #设置初始值
    targt = d[0]
    #设置count值
    count = 1
    for i in range(1,longth):
        if count == 0 :
            #当count为0 ，初始值为当前值
            targt = d[i]
            count = 1
        elif d[i] == targt:
            #当遍历的值为前一个值，count+1
            count += 1
        #当遍历的值不等于前一个值，count-1
        elif d[i] != targt:
            count -= 1
    #获得了理论上出现次数最多的数targe，进行校验
    counts = 0
    for j in range(longth):
        if d[j] == targt:
            counts += 1
    mid = len(d)//2
    if counts >= mid:
        print('列表中出现次数最多的为{},{}出现的次数为{}'.format(targt,targt,counts))
    else:
        return 0
if __name__ == "__main__":

        try:
            while True:
                b = [int(i) for i in input('输入列表').split(' ')]
                print('输入的列表为：%s'%b)
                print(FindMoreHalf(b))
                break
        except:
            pass

test001 = 10 * 2
test002 = 10 ** 2
print(test001,test002)
print('--'*20)
def count_digit(number):
    return len(str(number))

def countThree(digit):
    if not isinstance(digit,int):
        raise TypeError('number is not int')
    # digit = len(str(number))
    if(digit <=0):
        return 0
    if(digit ==1):
        return 1
    return 10*countThree(digit-1) + 10 **(digit-1)

print(countThree(count_digit(99)))


