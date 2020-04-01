import urllib.request
import csv
import codecs
import json
from bs4 import BeautifulSoup
def douban():
    print('爬取豆瓣的数据信息')
    print('-------start-------')
    headers = {"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
    # user_agent = {'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    url = 'https://www.douban.com/search?q=python'
    res = urllib.request.Request(headers = headers,url = url)
    ebook = urllib.request.urlopen(res).read().decode()
    # print(ebook)

    #通过bs4解析得到书本信息
    soup = BeautifulSoup(ebook,'lxml')

    #获取a标签的内容
    account = []
    a_text = soup.find_all('div',class_="title")
    for text in a_text:
        get_text = text.get_text()

        get_text.strip().replace('\n','')
        account.append(get_text)
    print(account)

    print('-'*10)


    print('ebook写入成功')




douban()