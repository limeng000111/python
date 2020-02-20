'''
练习4
▪ 输入一个字符串，返回满足以下条件字符串
■ 找到字符串中的子串 ‘not’ 和 'bad’
■ 如果 ‘bad’ 出现在 ‘not’ 后面，就把 ‘not’ … ‘bad’ 之间包含的所有字符串替换成 ‘good’
'''
def replace_str():
    str = 'Study is not only to learn, actually i think this is a bad way. '
    #print(str.index("not"))

    n = str.split(' ')
   # print(n)

        #print(i)
        #if i == 'not' and i == 'bad':
         #   print('not and bad are exist')
        #找到not的位置
    x = n.index('not')
    #print(x)
        #x = int(x)
        #找到bad的位置
    y = n.index('bad')
            #print('-----:',n)

    for z in range (x+1,y):
        #print('n:{}'.format(n))
        #print('z:{}'.format(z))
        #print(n[z])
        good = 'good'
        n[z] = good
    #print(n)
    n = ' '.join(n)
    print(n)


#replace_str()
'''
练习5
输入一个字符串，把字符串拆分成两个等分
■ 如果字符串长度是偶数，前一半和后一 半的长度是相同的
■ 如果字符串长度是奇数，则多出的一个 字符加到前一半，如:‘abcde’，前一半 是’abc’，后一半是’de’
'''
def str_two():
    n = 'aaaabbbb'
    num = len(n)
    if num % 2 == 0 :
        aver = num // 2
        a = n[:aver]
        b = n[aver:]
        print('前半段：{}，后半段：{}'.format(a,b))
    if num % 2 != 0 :
        aver = num //2
        print(type(aver))
        a = n[:aver+1]
        b = n[aver+1:]
        print('前半段：{},后半段：{}'.format(a,b))
#str_two()
'''
练习6
▪ 输入一个字符串返回满足以下条件的字符串
■ 找出与字符串的第一个字母相同的字母， 把它们替换成 ‘*’，除了第一个字母本身以外
■ 例如: 输入’babble’， 返回 'ba**le’
'''
def equal_str():
    n = input('请输入字符串:')
    num = n[0]
    s = n.replace(num,'*')
    res = num + s[1:]
    print(res)
#equal_str()
'''
练习7
▪ 输入一个字符串,返回满足以下条件的字符串
■ 由字符串的最前面两个字母和最后两个字母组成的字符串。
■ 例如: ‘spring’ 返回 ‘spng’， ‘is’ 返回 'is’
■ 当输入的字符串长度小于2时，返回空字符串
'''
def head_tail_word():
    str_input = input('请输入字符串:')
    longth = len(str_input)
    if longth > 2:
        res = str_input[:2]+str_input[-2:]
    elif longth == 2:
        res = str_input
    else:
        res= ''
    print(res)
#head_tail_word()

'''
这是大佬写的对blibli登陆页面，滑块验证码的自动化，希望有一天能写出来
'''
from selenium import webdriver
import time
import base64
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.ui import WebDriverWait
import random
import copy


class VeriImageUtil():

    def __init__(self):
        self.defaultConfig = {
            "grayOffset": 20,
            "opaque": 1,
            "minVerticalLineCount": 30
        }
        self.config = copy.deepcopy(self.defaultConfig)

    def updateConfig(self, config):
        # temp = copy.deepcopy(config)
        for k in self.config:
            if k in config.keys():
                self.config[k] = config[k]

    def getMaxOffset(self, *args):
        # 计算偏移平均值最大的数
        av = sum(args) / len(args)

        maxOffset = 0
        for a in args:
            offset = abs(av - a)
            if offset > maxOffset:
                maxOffset = offset
        return maxOffset

    def isGrayPx(self, r, g, b):
        # 是否是灰度像素点，允许波动offset
        return self.getMaxOffset(r, g, b) < self.config["grayOffset"]

    def isDarkStyle(self, r, g, b):
        # 灰暗风格
        return r < 128 and g < 128 and b < 128

    def isOpaque(self, px):
        # 不透明
        return px[3] >= 255 * self.config["opaque"]

    def getVerticalLineOffsetX(self, bgImage):
        # bgImage = Image.open("./image/bg.png")
        # bgImage.im.mode = 'RGBA'
        bgBytes = bgImage.load()

        x = 0
        while x < bgImage.size[0]:
            y = 0
            # 点》》线，灰度线条数量
            verticalLineCount = 0

            while y < bgImage.size[1]:
                px = bgBytes[x, y]
                r = px[0]
                g = px[1]
                b = px[2]
                # alph = px[3]
                # print(px)
                if self.isDarkStyle(r, g, b) and self.isGrayPx(r, g, b) and self.isOpaque(px):
                    verticalLineCount += 1
                else:
                    verticalLineCount = 0
                    y += 1
                    continue

                if verticalLineCount >= self.config["minVerticalLineCount"]:
                    # 连续多个像素都是灰度像素，直线，认为需要滑动这么多
                    # print(x, y)
                    return x

                y += 1

            x += 1
        pass


class DragUtil():
    def __init__(self, driver):
        self.driver = driver

    def __getRadomPauseScondes(self):
        """
        :return:随机的拖动暂停时间
        """
        return random.uniform(0.6, 0.9)

    def simulateDragX(self, source, targetOffsetX):
        """
        模仿人的拖拽动作：快速沿着X轴拖动（存在误差），再暂停，然后修正误差
        防止被检测为机器人，出现“图片被怪物吃掉了”等验证失败的情况
        :param source:要拖拽的html元素
        :param targetOffsetX: 拖拽目标x轴距离
        :return: None
        """
        action_chains = webdriver.ActionChains(self.driver)
        # 点击，准备拖拽
        action_chains.click_and_hold(source)
        # 拖动次数，二到三次
        dragCount = random.randint(2, 3)
        if dragCount == 2:
            # 总误差值
            sumOffsetx = random.randint(-15, 15)
            action_chains.move_by_offset(targetOffsetX + sumOffsetx, 0)
            # 暂停一会
            action_chains.pause(self.__getRadomPauseScondes())
            # 修正误差，防止被检测为机器人，出现图片被怪物吃掉了等验证失败的情况
            action_chains.move_by_offset(-sumOffsetx, 0)
        elif dragCount == 3:
            # 总误差值
            sumOffsetx = random.randint(-15, 15)
            action_chains.move_by_offset(targetOffsetX + sumOffsetx, 0)
            # 暂停一会
            action_chains.pause(self.__getRadomPauseScondes())

            # 已修正误差的和
            fixedOffsetX = 0
            # 第一次修正误差
            if sumOffsetx < 0:
                offsetx = random.randint(sumOffsetx, 0)
            else:
                offsetx = random.randint(0, sumOffsetx)

            fixedOffsetX = fixedOffsetX + offsetx
            action_chains.move_by_offset(-offsetx, 0)
            action_chains.pause(self.__getRadomPauseScondes())

            # 最后一次修正误差
            action_chains.move_by_offset(-sumOffsetx + fixedOffsetX, 0)
            action_chains.pause(self.__getRadomPauseScondes())

        else:
            raise Exception("莫不是系统出现了问题？!")

        # 参考action_chains.drag_and_drop_by_offset()
        action_chains.release()
        action_chains.perform()

    def simpleSimulateDragX(self, source, targetOffsetX):
        """
        简单拖拽模仿人的拖拽：快速沿着X轴拖动，直接一步到达正确位置，再暂停一会儿，然后释放拖拽动作
        B站是依据是否有暂停时间来分辨人机的，这个方法适用。
        :param source:
        :param targetOffsetX:
        :return: None
        """

        action_chains = webdriver.ActionChains(self.driver)
        # 点击，准备拖拽
        action_chains.click_and_hold(source)
        action_chains.pause(0.2)
        action_chains.move_by_offset(targetOffsetX, 0)
        action_chains.pause(0.6)
        action_chains.release()
        action_chains.perform()

def checkVeriImage(driver):
    WebDriverWait(driver, 5).until(
        lambda driver: driver.find_element_by_css_selector('.geetest_canvas_bg.geetest_absolute'))
    time.sleep(1)
    im_info = driver.execute_script(
        'return document.getElementsByClassName("geetest_canvas_bg geetest_absolute")[0].toDataURL("image/png");')
    # 拿到base64编码的图片信息
    im_base64 = im_info.split(',')[1]
    # 转为bytes类型
    im_bytes = base64.b64decode(im_base64)
    with open('./temp_bg.png', 'wb') as f:
        # 保存图片到本地
        f.write(im_bytes)

    image_data = BytesIO(im_bytes)
    bgImage = Image.open(image_data)
    # 滑块距离左边有 5 像素左右误差
    offsetX = VeriImageUtil().getVerticalLineOffsetX(bgImage)
    print("offsetX: {}".format(offsetX))
    if not type(offsetX) == int:
        # 计算不出，重新加载
        driver.find_element_by_css_selector(".geetest_refresh_1").click()
        checkVeriImage(driver)
        return
    elif offsetX == 0:
        # 计算不出，重新加载
        driver.find_element_by_css_selector(".geetest_refresh_1").click()
        checkVeriImage(driver)
        return
    else:
        dragVeriImage(driver, offsetX)


def dragVeriImage(driver, offsetX):
    # 可能产生检测到右边缘的情况
    # 拖拽
    eleDrag = driver.find_element_by_css_selector(".geetest_slider_button")
    dragUtil = DragUtil(driver)
    dragUtil.simulateDragX(eleDrag, offsetX - 10)
    time.sleep(2.5)

    if isNeedCheckVeriImage(driver):
        checkVeriImage(driver)
        return
    dragUtil.simulateDragX(eleDrag, offsetX - 6)

    time.sleep(2.5)
    if isNeedCheckVeriImage(driver):
        checkVeriImage(driver)
        return
    # 滑块宽度40左右
    dragUtil.simulateDragX(eleDrag, offsetX - 56)

    time.sleep(2.5)
    if isNeedCheckVeriImage(driver):
        checkVeriImage(driver)
        return
    dragUtil.simulateDragX(eleDrag, offsetX - 52)

    if isNeedCheckVeriImage(driver):
        checkVeriImage(driver)
        return


def isNeedCheckVeriImage(driver):
    if driver.find_element_by_css_selector(".geetest_panel_error").is_displayed():
        driver.find_element_by_css_selector(".geetest_panel_error_content").click();
        return True
    return False


def task():
    # 此步骤很重要，设置chrome为开发者模式，防止被各大网站识别出来使用了Selenium
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])

    options = webdriver.FirefoxOptions()

    # driver = webdriver.Firefox(executable_path=r"../../../res/webdriver/geckodriver_x64_0.26.0.exe",options=options)
    driver = webdriver.Firefox(executable_path=r"../../../res/webdriver/geckodriver_x64_0.26.0.exe",options=options)

    driver.get('https://passport.bilibili.com/login')
    time.sleep(3)

    driver.find_element_by_css_selector("#login-username").send_keys("1234567")
    driver.find_element_by_css_selector("#login-passwd").send_keys("abcdefg")
    driver.find_element_by_css_selector(".btn.btn-login").click()
    time.sleep(2)
    checkVeriImage(driver)

    pass


#   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
def isElementExist(driver, css):
    try:
        driver.find_element_by_css_selector(css)
        return True
    except:
        return False


if __name__ == '__main__':
    task()






