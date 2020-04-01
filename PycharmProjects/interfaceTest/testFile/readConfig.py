import os
import codecs
import configparser

config = configparser.ConfigParser()
config.read('ini', encoding='utf-8')
print(config.sections())
#当前文件路径
proDir = os.path.split(os.path.realpath(__file__))[0]
#在当前文件路径下查找.ini几件
configPath = os.path.join(proDir,'config.ini')
print(configPath)

conf = configparser.ConfigParser()

#读取.ini
conf.read(configPath)
#get()函数读取section里面的参数值
url = conf.get('HTTP','baseurl')

print(url)
print(conf.sections())
print(conf.options('HTTP'))
print(conf.items('HTTP'))

# remove BOM
class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath,'w')
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self,name):
        value = self.cf.get('EMAIL' , 'mail_user')
        return value

    def get_HTTP(self,url):
        value = self.cf.get('HTTP','baseurl')
        return value

