import os
import sys
import platform

#判断系统环境，添加了环境变量，调用了主业务区main.py

print(platform.platform())
print(platform.node())
print(platform.system())

if platform.system() == 'Windows':
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])

else:
    BASE_DIR = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])

sys.path.insert(0,BASE_DIR)

from core import main
from conf import setting

if __name__ == '__main__':
    obj = main.Manage_center()
    obj.run()