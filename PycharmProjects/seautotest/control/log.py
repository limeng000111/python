import datetime
from pathlib import Path
import logging
import sys
from control.utlis import mkdir

#当前时间
def today():
    date = datetime.datetime.now()
    #print(date)
    #print(date.strftime('%Y%m%d'))
    return date.strftime('%Y%m%d')

#获取logger实例，如果参数为空，默认返回root logger
logger = logging.getLogger('seautotest')

#指定logger输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s : %(message)s')

#创建文件夹
mkdir('log')

#文件日志
log_file = str(Path('log') / '{}.log'.format(today()))
print(log_file)

file_handler = logging.FileHandler(log_file,mode='a',encoding='utf-8',delay=False)
file_handler.setFormatter(formatter)

console_hanlder = logging.StreamHandler(sys.stdout)
console_hanlder.formatter = formatter

#为日志添加处理器
logger.addHandler(file_handler)
logger.addHandler(console_hanlder)

#指定日志输出最低级别
logger.setLevel(logging.INFO)