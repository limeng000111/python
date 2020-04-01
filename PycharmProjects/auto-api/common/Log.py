import logging
from datetime  import datetime
import threading
import os

class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = os.path.split(os.path.realpath(__file__))[0]
        resultPath = os.path.join(proDir,'result')
        #if not exist result ,creat it
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        logPath = os.path.join(resultPath,str(datetime.now().strftime('%Y_%m_%d  %H:%M%S')))
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        #初始化logger
        logger = logging.getLogger()
        #设置log等级
        logger.setLevel(logging.INFO)
        #定义handle
        handle = logging.FileHandler(os.path.join(logPath,'out.log'))
        #定义formatter
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        #定义formatter
        handle.setFormatter(formatter)
        #添加handler
        self.logger.addHandle(handle)

class Mylog:
    log = None
    cxtx = threading.Lock()

    def __init__(self):
        pass


    @staticmethod
    def get_log():
        if Mylog.log == None:
            Mylog.cxtx.acquire()
            Mylog.log = Log()
            Mylog.cxtx.release()

        return Mylog.log

