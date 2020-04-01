import os
import sys
import shelve
from conf import setting


class Manage_center(object):
    def __init__(self):
        pass

    def run(self):
        while True:
            print("\n欢迎进入CLASS_SYSTEM系统\n"
                  "1 学生视图\n"
                  "2 教师视图\n"
                  "3 学校视图\n"
                  "q 退出学员管理系统\n")

            user_choice = input(">>>请输入您需要的模块")
            if user_choice == '1':
                Manage_student()
            elif user_choice == '2':
                Manage_tercher()
            elif user_choice == '3':
                Manage_school()
            elif user_choice == 'q':
                print("欢迎下次使用")
                break
            else:
                print("请输入正确的字母或者数字")

class Manage_student():
    '''学校管理视图'''
    def __init__(self):
        if os.path.exists(setting.school_db_file+'.dat'):     #shelve生成文件以.dat结尾
            self.school_db = shelve.open(setting.school_db_file)   #打开学校数据库文件
            self.school_db.close()
        else:
            print("\系统信息：初始化数据库 ")
            self.initialize_school()
            self.run_manage()
            self.school_db.close()
    def initialize_school(self):
        '''实例化两个学校北京/上海'''
        self.school_db = shelve.open(setting.school_db_file)
        self.school_db['北京'] = School('北京','中国.北京')
        self.school_db['上海'] = School('上海','中国.上海')

    def run_manage(self):
        '''运行学校管理视图'''
        while True:
            for key in self.school_db:
                print("学校：",key)
            choice_school = input(">>>输入管理的学校名")
            self.school_obj = self.school_db[choice_school]
            while True:
                print("\n欢迎来到%s校区\n"
                      "添加课程\n"
                      "增加老师\n"
                      "招聘讲师\n"
                      "查看课程\n"
                      "查看班级\n"
                      "查看讲师\n"
                      "退出程序 exit " % self.school_obj.school_name)

                user_func = input(">>>输入操作的命令").strip()
                if hasattr(self,user_func):
                    getattr(self,user_func)()
        else:
            print("输入错误，请输入正确的学校名")

def add_class(self):
    class_name = input("输入要添加班级的名称").strip()
    couser_name = input("输入要关联的课程名称").strip()
    if class_name not in self.school_obj.school_class:
        if couser_name in self.school_obj.school_course:
            couser_obj = self.school_obj.school_course[couser_name]
            self.school_obj.create_class(class_name,couser_name)
            self.school_db.update({self.choice_school:self.school_obj})#更新数据库
            print("班级创建成功")
        else:
            print("系统错误,关联的课程不存在")
    else:
        print("系统错误，关联的课程已存在")

def add_tercher(self):
    tercher_name = input("输入要招聘老师的名称").strip()
    tercher_salary = input("输入老师的薪资").strip()
    tercher_class = input("输入要关联的班级").strip()

    if tercher_class in self.school_obj.school_class:#判断班级是否存在
        class_obj = self.school_obj.school_class[tercher_class]
        if tercher_name not in self.school_obj.school_tercher:
            self.school_obj.create_tercher(tercher_name,tercher_class)
            print("新老师招聘成功")
        else:
            self.school_obj.update_tercher(tercher_name,tercher_class)





# class Manage_tercher():
# class Manage_school():
