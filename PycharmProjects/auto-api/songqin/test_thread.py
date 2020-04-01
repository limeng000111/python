import _thread
import time
def thread(threadname,delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count += 1
        print(threadname,time.ctime(time.time()))
        print('it is over')

try:
    _thread.start_new_thread(thread,('thread-001',2,))
    _thread.start_new_thread(thread,('thread-002',4,))


except:
    print('线程无法启动')

while 1:
    pass






