#-*- coding:utf-8 -*-
import os
import configparser as cparser
import pymysql
import logging
import auto_api.log.log as log


logger = log.logger
# logger = logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(message)s')
#获取配置文件信息
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\','/')
file_path = base_dir + '/mysql/db_config.ini'
logger.info(file_path)
# print(file_path)
# logger.INFO(file_path)

#初始化获取配置信息的实例
cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get('mysql','host')
user = cf.get('mysql','user')
passwd = cf.get('mysql','passwd')
port = cf.get('mysql','port')


#连接mysql，并执行操作

#类名称首字母需要大写
class Connect_db():
    def __init__(self):
        try:
            self.connection = pymysql.connect(host = host,port = int(port),user = user,passwd = passwd,charset = 'utf8', cursorclass = pymysql.cursors.DictCursor)
            logger.info('连接成功')
        except pymysql.err.OperationalError as e:
            print("mysql error %d:%s"%(e.args[0],e.args[1]))

    def query_db(self,sql):

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result_sql = cursor.fetchall()
            self.connection.commit()
            return result_sql

if __name__ == '__main__':
    t = Connect_db()






