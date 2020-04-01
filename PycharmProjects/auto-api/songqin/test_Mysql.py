#-*-coding:utf-8-*-
import pymysql

#打开数据库链接
db = pymysql.connect(host = '172.19.242.72',user = 'cnsellers',password = 'cnsellers!@##@!',database = 'bizpal')

#使用cursor()方法获取游标
cursor = db.cursor()

#执行sql语句
sql = '''
INSERT INTO `bizpal`.`cn_user_invitation`(`user_id`, `invitation_code`, `invitation_user_id`, `user_ip`, `browser`, `reg_type`, `invitation_type`, `create_time`) VALUES (1572313561, 'PJ3FCM', 1569315027, '192.168.246.4', 'Chrome', 12, 0, 1572313561);
'''

try:
    #执行sql语句
    cursor.execute(sql)
    db.commit()
    print('sql执行成功')
except:
    #发生错误，回滚
    db.rollback()


#使用fetchone获取一条数据
data = cursor.fetchall()

print(data)

#关闭数据库链接
db.close()