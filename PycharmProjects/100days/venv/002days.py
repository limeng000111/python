#-*-coding:UTF-8-*-
# import time
#
# class Color(object):
#     def __init__(self,second=0,minute=0,hour=0):
#         self.second = second
#         self.minute = minute
#         self.hour = hour
#
#     def run(self):
#         #60s=1min
#         #60min = 1h
#         self.second += 1
#         if self.second == 60:
#             self.second = 0
#             self.minute += 1
#             if self.minute == 60:
#                 self.minute = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0
#
#     def shown(self):
#         #%02d :字符串长度为2，不足2的用0补充
#         # return '%02d:%02d%:02d' % \
#         #        (self.hour,self.minute,self.second)
#           return '%02d:%02d:%02d' % \
#                (self.hour, self.minute, self.second)
#
# def main():
#     color = Color(11,59,23)
#     while True:
#         print(color.shown())
#         time.sleep(1)#1s的变化
#         color.run()
#
# if __name__ == '__main__':
#     main()
from math import sqrt
#
# class Point(object):
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#
#     def move_to(self):
#         self.x = x
#         self.y = y
#
#     def move_by(self):
#         self.x += dx
#         self.y += dy
#
#     def distince(self,other):
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx**2 + dy**2)
#
# def main():
#     p1=Point(2,2)
#     p2=Point(3,3)
#     print(p1.distince(p2))
#
# if __name__ == '__main__':
#     main()


#@property装饰器:私有属性可以通过属性的getter()和setter()方法调用
class Person():
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self,age):
        self._age = age
        
    def play(self):
        if self._age < 20:
            print('%s is playing baketball' % self.name)
        else:
            print('%s is working' % self.name)

def main():
    person1 = Person('jack',13)
    # person2 = Person('rose',24)
    print(person1.play())
    # print(person2.play())
    person1.age = 24
    print(person1.play())

if __name__ == '__main__':
    main()





