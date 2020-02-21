#!/usr/bin/env python
# -*-coding:utf-8-*-
#time    :  2020-02-21
#@Author :  limeng
#@Email  :  2421712196@qq.com
#@Note   :  类似黑客帝国的代码雨效果


#导入系统文件库
import pygame
import random
from pygame.locals import *
from random import randint


#定义窗体参数及加载字体文件
SCREEN_WIDTH = 900   #窗体宽度
SCREEN_HEIGHT = 600  #窗体高度
LOW_SPEED = 4        #字体移动最低速度
HIGH_SPEED = 10      #字体移动最快速度
FONT_COLOR =(00,150,00)#字体颜色
FONT_SIZE = 5        #字体尺寸
FONT_NUM = 20        #显示字体数量
FONT_NAME = "calibrii.ttf" #注意字体的文件名必须和真实文件完全相同（注意大小写，文件名不能是中文）
FREQUENCE = 10       #时间频度
times = 0            #初始化时间

#定义随机参数
def randomspeed():
    return randint(LOW_SPEED,HIGH_SPEED)
def randomposition():
    return randint(0,SCREEN_WIDTH),randint(0,SCREEN_HEIGHT)
def randomname():
    return randint(0,10000)
def randomvalue():
    return randint(0,100)

class Word(pygame.sprite.Sprite):
    def __init__(self,bornposition):
        pygame.sprite.Sprite.__init__(self)
        self.value = randomvalue()
        self.font = pygame.font.Font(FONT_NAME,FONT_SIZE)
        self.image = self.font.render(str(self.value),True,FONT_COLOR)
        self.speed = randomspeed()
        self.rect = self.image.get_rect()
        self.rect.topleft = bornposition

    def update(self):
        self.rect = self.rect.move(0,self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('ViatorSun CodeRain')
clock = pygame.time.Clock()
group = pygame.sprite.Group()
group_count = int(SCREEN_WIDTH / FONT_NUM)

#mainloop
while True:
    time = clock.tick(FREQUENCE)
    for even in pygame.event.get():
        if even.type == QUIT :
            pygame.quit()
            exit()

    screen.fill((0,0,0))
    for i in range(0,group_count):
        group.add(Word((i*FONT_NUM,-FONT_NUM)))

    group.update()
    group.draw(screen)
    pygame.display.update()