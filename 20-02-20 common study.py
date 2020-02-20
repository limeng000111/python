'''
练习4
▪ 输入一个字符串，返回满足以下条件字符串
■ 找到字符串中的子串 ‘not’ 和 'bad’
■ 如果 ‘bad’ 出现在 ‘not’ 后面，就把 ‘not’ … ‘bad’ 之间包含的所有字符串替换成 ‘good’
'''
def replace_str():
    str = 'Study is not only to learn, actually i think this is a bad way. '
    #print(str.index("not"))

    n = str.split(' ')
   # print(n)

        #print(i)
        #if i == 'not' and i == 'bad':
         #   print('not and bad are exist')
        #找到not的位置
    x = n.index('not')
    #print(x)
        #x = int(x)
        #找到bad的位置
    y = n.index('bad')
            #print('-----:',n)

    for z in range (x+1,y):
        #print('n:{}'.format(n))
        #print('z:{}'.format(z))
        #print(n[z])
        good = 'good'
        n[z] = good
    #print(n)
    n = ' '.join(n)
    print(n)


#replace_str()
'''
练习5
输入一个字符串，把字符串拆分成两个等分
■ 如果字符串长度是偶数，前一半和后一 半的长度是相同的
■ 如果字符串长度是奇数，则多出的一个 字符加到前一半，如:‘abcde’，前一半 是’abc’，后一半是’de’
'''
def str_two():
    n = 'aaaabbbb'
    num = len(n)
    if num % 2 == 0 :
        aver = num // 2
        a = n[:aver]
        b = n[aver:]
        print('前半段：{}，后半段：{}'.format(a,b))
    if num % 2 != 0 :
        aver = num //2
        print(type(aver))
        a = n[:aver+1]
        b = n[aver+1:]
        print('前半段：{},后半段：{}'.format(a,b))
#str_two()
'''
练习6
▪ 输入一个字符串返回满足以下条件的字符串
■ 找出与字符串的第一个字母相同的字母， 把它们替换成 ‘*’，除了第一个字母本身以外
■ 例如: 输入’babble’， 返回 'ba**le’
'''
def equal_str():
    n = input('请输入字符串:')
    num = n[0]
    s = n.replace(num,'*')
    res = num + s[1:]
    print(res)
#equal_str()
'''
练习7
▪ 输入一个字符串,返回满足以下条件的字符串
■ 由字符串的最前面两个字母和最后两个字母组成的字符串。
■ 例如: ‘spring’ 返回 ‘spng’， ‘is’ 返回 'is’
■ 当输入的字符串长度小于2时，返回空字符串
'''





