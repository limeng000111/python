from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
 </div>
'''
# #初始化xpath对象
# html = etree.HTML(text)
# #解析对象输出代码
# result = etree.tostring(html,encoding='utf-8')

#etree.parse是一个解析器，修复HTML中缺少的元素
html = etree.parse(r'C:\Users\dell\Desktop\xml.html',etree.HTMLParser())
#将html中的元素解析成字节
result = etree.tostring(html)
#将html中的元素解析成列表
result1 = etree.tostringlist(html)
#打印文本中所有的节点元素
element = html.xpath('//*')

print(type(html))
print(type(result))
#打印经过处理后的代码
#etree会自动修复缺少的的文本节点
print(result.decode('utf-8'))
print(result1)
print(element)

print('-'*20+'这是分隔符'+'-'*20)

#!/usr/bin/env  python
#coding :utf-8
import urllib.request
import json
from lxml import etree
import urllib.error


def one_to_page(html):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    try:
        respose =urllib.request.Request(html,headers=headers)
        html = urllib.request.urlopen(respose)
        result = html.read().decode('utf-8')
    except urllib.error as e:
        print('request is error!' ,e )

    try:
        html1 = etree.HTML(result,etree.HTMLParser())#解析获取的内容
        #获取列表中的数据
        result1 = html1.xpath('//table[contains(@class,"table-top20")]/tbody/tr//text()')

        pos = 0
        for i in range(20):
            if i == 0:
                yield  result1[i:5]
            else:
                yield result1[pos:pos+5]  #返回排名生成器数据
            pos += 5
    except etree.ParseError as e:
        print(e.position)

def write_file(data):#将数据重新组合成字典

    for i in data:
        if len(i[0]) == 1:
            i[0] = i[0] + ' '
        if len(i[1]) == 1:
            i[1] = i[1] + ' '
        sul = {
            '2019年6月排行':i[0],
            '2018年6月排行':i[1],
            '开发语言':i[2],
            '评级':i[3],
            '变化率':i[4]
        }


        with open(r'c:/Users/dell/Desktop/exercise.txt','a',encoding='utf-8') as fp:
            fp.write(json.dumps(sul,ensure_ascii=False) + '\n')#需要格式化数据
            fp.close()
        print(sul)
    return None
def main():
    url = 'https://www.tiobe.com/tiobe-index/'
    data = one_to_page(url)
    revalue=write_file(data)
    if revalue == None:
        print('ok')

if __name__ == '__main__':
    main()


