#计算密集型任务，例如：计算，视频解码，全靠cpu的运算能力
#计算型任务使用多进程，I/O密集型任务使用多线程
#单线程

import os ,time
'''
def task():
    ret = 0
    for i in range(100000000):
        ret *= i

if __name__ == '__main__':
    print('本机是 {} 核CPU'.format(os.cpu_count()))
    start_time = time.time()
    for u in range(5):
        task()
    end_time = time.time()
    print('单线程运行时间为：{}'.format(end_time-start_time))

#多线程

import os, time
from threading import Thread


def task():
    ret = 0
    for i in range(100000000):
        ret *= i


if __name__ == '__main__':
    arr = []
    print('本机是 {} 核CPU'.format(os.cpu_count()))
    start_time = time.time()
    for u in range(5):
        thread_test = Thread(target=task)

        arr.append(thread_test)
        thread_test.start()
    for i in arr:
        i.join()
    end_time = time.time()
    print('多线程运行时间为：{}'.format(end_time - start_time))

#多进程
import os, time
from multiprocessing import Process


def task():
    ret = 0
    for i in range(100000000):
        ret *= i


if __name__ == '__main__':
    arr = []
    print('本机是 {} 核CPU'.format(os.cpu_count()))
    start_time = time.time()
    for u in range(5):
        thread_test = Process(target=task)

        arr.append(thread_test)
        thread_test.start()
    for i in arr:
        i.join()
    end_time = time.time()
    print('多进程运行时间为：{}'.format(end_time - start_time))


#简易的单生产模型  单消费模型
import queue
from threading import Thread
class P_Consumer():
    #定义生产者模型
    def product_test(threadName,q):
        for i in range(10):
            product = 'product' + str(i)

            q.put(product)
            print('线程 {} 生产数据 {} '.format(threadName,product))
            time.sleep(1)
        q.join()


    #定义消费者模型
    def consumer_test(threadName,q):
        while True:
            product = q.get()
            print('线程{} 获取数据{}'.format(threadName,product))
            q.task_done()

    q = queue.Queue()
    thread1 = Thread(target=product_test,args=('product_one',q))
    thread2 = Thread(target=consumer_test,args=('consumer_one',q))

    thread2.setDaemon(True)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

import queue

def test_queue():
    q = queue.Queue(maxsize=1)
    q.put(100,True,2)
#test_queue()

#线程池
import time
import threadpool
import threading

def sayhello(name):
    print('%s say hello to %s'%(threading.current_thread().getName(),name))
    time.sleep(1)
    return name

#定义回调函数,用于取回结果
def callback(request,result):
    print('callback result = %s'%result)

name_list = ['admin','root','scott','tiger']
start_time = time.time()
pool = threadpool.ThreadPool(2)#创建线程池
requests = threadpool.makeRequests(sayhello,name_list,callback)#创建任务
[pool.putRequest(req) for req in requests]#加入任务
pool.wait()
print('%s cost time is %s '%(threading.current_thread().getName(),time.time()-start_time))
'''
from urllib.request import urlopen
import urllib.request
import urllib.error

try:
    response = urlopen('http://admin.demobizpal.com/admin/Service/index')
   # print(response.read().decode('utf-8'))

except urllib.error.URLError as e:
    print(e.reason)

import urllib
from urllib import parse
url = 'http://www.baidu.com/+爬虫'
result = urllib.parse.quote(url,'+')#更改safe参数
print(result)

import urllib
base_url = 'http://www.baidu.com'
url = 'https://www.google.com/urllib.parse.html;python?kw=urllib.parse#module-urllib'
result = urllib.parse.urljoin(base_url,url,False)
print(result)

# 创建 GET 请求
import urllib
params = {'username':'xxx','password':'123'}
base_url='http://www.baidu.com'
url=base_url + '?' + urllib.parse.urlencode(params)
print(url)
params = {'username':['xxx', 'yyy'], 'password':'123'} # username 键对应多个值
base_url='http://www.baidu.com'
url=base_url + '?' + urllib.parse.urlencode(params) # doseq 设置为 False，会解析成乱码
print(url)
url=base_url + '?' + urllib.parse.urlencode(params) # doseq 设置为 True
print(url)

