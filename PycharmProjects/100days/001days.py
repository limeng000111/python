#author:limeng
#data:2019-8-1
# username = input('>>>')
# password = input('>>>')
#
# #校验密码是否正确
# if username == 'limeng' and password == '123456':
#     print('pass')
# else :
#     print('failed')

#
# from random import randint
# for i in range(10):
#     num = randint(0,10)
#     if num == 1:
#        result = 'sing'
#     elif num == 2:
#         result = 'dance'
#     elif num == 3:
#         result = 'drink'
#     else:
#         result = 'next'
#     print(result)
# #     print('sing:',result.count('sing'))
# #     print('dance:', result.count('dance'))
# #     print('drink:', result.count('drink'))
# # sum = 0
# # for i in range(1,101,2):
# #     sum += i
# #     print(sum)
# from random import randint
#
# conputer = randint(1,101)
# print(conputer)
# count = 0
# while True:
#     count += 1
#     person = int(input('>>>'))
#     if person == conputer:
#         print('got it')
#     elif conputer > person:
#         print('小了一点')
#     else:
#         print('大了一点')
# #         break
# #     if count > 7:
# #         print('智商较低')
# def narcissistic_number_1(num):
#     length = len(str(num))
#     count = length
#     num_sum = 0
#     while count:
#         num_sum += ((num // 10 ** (count -1)) % 10) ** length
#         count -= 1
#     else:
#         if num_sum == num :
#             print("%d is %d bit narcissistic_number" % (num,length))
#         else:
#             print("%d is not a narcissistic_number" % num)
#
# max_num = int(input('请输入最大范围'))
#
# for num in range(0,max_num):
#     narcissistic_number_1(max_num)
# import os
# import sys
# import time
# def main():
#     content ='北京欢迎您...'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:]+ content[0]
#         # print(content[0])
# if __name__ == '__main__':
#     main()
# from random import randint
# def roll_dice(n):
#     total = 0
#     for _  in range(n):
#         total += randint(1,6)
#     return total
# print(roll_dice(2))
# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def study(self,course_name):
#         print("%s is studying %s" % ( self.name,course_name))
#
#     def watch_movie(self,age):
#         if age < 18:
#             print(" %s watching beer" % (self.name))
#         else:
#             print('%s please go to work' % (self.name))
# def main():
#     stu1 = Student('李萌', 25)
# #     stu1.study('python教程')
# #     stu1.watch_movie(25)
# #
# # if __name__ == '__main__':
# #     main()
#
# from abc import ABCMeta,abstractmethod
#
# class Pet(object,metaclass=ABCMeta):
#     #抽象类，专门用于给子类继承
#     def __init__(self,nickname):
#         self._nickname = nickname
#
#     @abstractmethod
#     def make_vioce(self):
#         #发出声音
#         pass
#
# class Dog(Pet):
#     def make_vioce(self):
#         print('%s : 汪汪汪' % self._nickname)
#
# class Cat(Pet):
#     def make_vioce(self):
#         print('%s : 喵喵喵' % self._nickname)
#
# def main():
#     pets = [Dog('旺财'),Cat('小花'),Dog('飞黄')]
#     for pet in pets:
#         print(pet.make_vioce())
#
# if __name__ == '__main__':
#     main()

import random

class Card():
    def __init__(self,suite,face):
        self._suite = suite
        self._face = face
    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        if 








