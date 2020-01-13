'''
data:2020-01-14
'''
#利用函数递归的方式，将输入的5个字符倒序打印出来

def fact(i):
    string = input('请输入字符串')
    if i == -1:
        return ''  #返回值必须要有  返回空会报错
    else:
        return string[i] + fact(i-1)#使用递归获取倒叙排列的值
#print(fact(len(string)-1))#请注意从0开始，最后一个值取不到

#5个人，第一个人10岁，第二个比第一个大2岁，第三个比第二个大2岁...请问第5个人多大（递归）
def age(n):
    if n == 1:
        return 10
    else:
        return age(n-1)+2
print(age(5))