import os
import codecs
import configparser

#当前目录
proDir = os.path.split(os.path.realpath(__file__))[0]
# print(proDir)
configPath = os.path.join(proDir,'config.ini')

class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[:3]
            file = codecs.open(configPath,'w')
            file.write(data)
            file.close()
        file.close()


        #ConfigParser 初始化对象
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    #获取配置文件中的名称
    def get_database(self,name):
        value = self.cf.get('DATABASE')
        return value

    def get_http(self,name):
        value = self.cf.get('HTTP')
        return value

    def get_email(self,name):
        value = self.cf.get('EMAIL')
        return value
