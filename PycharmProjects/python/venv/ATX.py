# #-*-coding:UTF-8-*-
# import uiautomator2 as u2
#
# u = u2.connect_usb()
# u.make_toast("hello world",3)
# coding: utf-8
# coding: utf-8
import unittest
import uiautomator2 as u2
import time
import uiautomator2.ext.htmlreport as htmlreport
from atx.ext.chromedriver import ChromeDriver
import cv2
import random
# class TestCloudMusic(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.u = u2.connect_usb('66J0218C03005237')
#         cls.u.set_fastinput_ime(True)
#         cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
#         hrp = htmlreport.HTMLReport(cls.u, 'report')
#         hrp.patch_click()
#
#         # cls.u.disable_popups(True)  # 允许自动处理弹出框
#         cls.u.toast.show("测试开始", 3)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.u.toast.show("测试结束", 3)
#         cls.u.app_stop_all()
#         cls.u.service(
#             "uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行
#
#     def setUp(self):
#         self.d = self.u.session("com.zjiec.sellingworld",attach=True)  # restart app
#
#         time.sleep(5)  # 等待首页广告结束
#
#     def tearDown(self):
#         pass
#
#     def testPrivateFM(self):  # 私人FM
#         self.d(text="服务资源").click()
#
#     def testRecommendEveryday(self):  # 每日推荐
#         self.d(text="交易市场").click()
import uiautomator2 as u2
from atx.ext.chromedriver import ChromeDriver

d = u2.connect_usb('66J0218C03005237')
d.set_fastinput_ime(True)

#通过wifi连接
#d.app_start("com.zjiec.sellingworld")
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/nested_scrollview"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
d.implicitly_wait(10)
#手机主页找到畅销天下
d(text="畅销天下").click()
#点击登录 进入登录页面
try:
    # 手机号账号密码登录
    d(resourceId="com.zjiec.sellingworld:id/mobile_phone_et").click()
    d.send_keys("18888888888", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/get_sms_code_btn").click()
    d(resourceId="com.zjiec.sellingworld:id/sms_code_et").click()
    d.send_keys("363636", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/login_btn").click()






    d.xpath(
        '//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
    # 上拉展示：退出登录按钮
    d.drag(42, 2000,42, 0,1)
    d(resourceId="com.zjiec.sellingworld:id/loginout_btn").click()

    # 再次切换至首页登录页面
    # 手机号密码登录
    d(resourceId="com.zjiec.sellingworld:id/pw_login_tv").click()
    d(resourceId="com.zjiec.sellingworld:id/mobile_phone_et_by_pw").click()
    d.send_keys("18888888888", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/password_et").click()
    d.send_keys("123456", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/pw_login_btn").click()
    # 切换至个人中心，退出登录
    d.xpath(
        '//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
    # 上拉展示：退出登录按钮
    d.drag(42, 2000,42, 0,1)
    d(resourceId="com.zjiec.sellingworld:id/loginout_btn").click()
    # 邮箱账号密码登录
    d(resourceId="com.zjiec.sellingworld:id/pw_login_tv").click()
    d(resourceId="com.zjiec.sellingworld:id/goto_email_id_login_btn").click()
    d(resourceId="com.zjiec.sellingworld:id/email_id_et").click()
    d.send_keys("2421712196@qq.com", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/email_id_pw_et").click()
    d.send_keys("123456", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/email_id_pw_login_btn").click()
    # 切换至个人中心，退出登录
    d.xpath(
        '//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
    # 上拉展示：退出登录按钮
    d.drag(42, 2000,42, 0,1)
    d(resourceId="com.zjiec.sellingworld:id/loginout_btn").click()

    # ID登录
    d(resourceId="com.zjiec.sellingworld:id/pw_login_tv").click()
    d(resourceId="com.zjiec.sellingworld:id/goto_email_id_login_btn").click()
    d(resourceId="com.zjiec.sellingworld:id/email_id_et").click()
    d.send_keys("lm8888lm", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/email_id_pw_et").click()
    d.send_keys("123456", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/email_id_pw_login_btn").click()
    # 切换至个人中心，退出登录
    d.xpath(
        '//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
    # 上拉展示：退出登录按钮
    d.drag(42, 2000,42, 0,1)
    d(resourceId="com.zjiec.sellingworld:id/loginout_btn").click()
    # 邮箱注册
    d(resourceId="com.zjiec.sellingworld:id/email_register_btn").click()
    d(resourceId="com.zjiec.sellingworld:id/email_et").click()


    l = []

    for i in range(6):
        rand_num = random.randint(0, 9)
        l.append(str(rand_num))

    qq_email = ''.join(l) + '@qq.com'
    # d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/email_et"]').click()
    # d.send_keys(qq_email, clear=True)
    # d(resourceId="com.zjiec.sellingworld:id/get_sms_code_btn").click()
    # d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/code_et"]').click()
    # d.send_keys("363636", clear=True)

    d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/email_et"]').click()
    d.send_keys(qq_email, clear=True)
    d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/get_sms_code_btn"]').click()
    d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/code_et"]').click()
    d.send_keys("363636", clear=True)


    d(resourceId="com.zjiec.sellingworld:id/register_btn").click()
    # 进入完善信息页面，填写密码，姓名和国家/地区
    d(resourceId="com.zjiec.sellingworld:id/password_et").click()
    d.send_keys("123456", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/name_et").click()
    d.send_keys("q", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/ok_btn").click()
    d(resourceId="com.zjiec.sellingworld:id/image").click()
    d(resourceId="com.zjiec.sellingworld:id/tv_cancel").click()
    time.sleep(20)


    # 切换至个人中心，退出登录
    d.xpath(
        '//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
    # 上拉展示：退出登录按钮
    d.drag(42, 2000,42, 0,1)
    d(resourceId="com.zjiec.sellingworld:id/loginout_btn").click()
    time.sleep(2)

    d(resourceId="com.zjiec.sellingworld:id/pw_login_tv").click()
    d(resourceId="com.zjiec.sellingworld:id/forget_pw_btn").click()
    d(resourceId="com.zjiec.sellingworld:id/mobile_et").click()
    d.send_keys("18856213800", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/get_sms_code_btn").click()
    d(resourceId="com.zjiec.sellingworld:id/code_et").click()

    d.send_keys("363636", clear=True)
    time.sleep(20)
    d(resourceId="com.zjiec.sellingworld:id/password_et").click()
    d.send_keys("123456", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/re_password_et").click()
    d.send_keys("123456", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/ok_btn").click()
    d(resourceId="com.zjiec.sellingworld:id/no_pw_login_tv").click()
    # 切换语言为英文
    # 邮箱登录
    d(resourceId="com.zjiec.sellingworld:id/language_tv").click()
    d(resourceId="com.zjiec.sellingworld:id/language_name", text="English").click()
    d(resourceId="com.zjiec.sellingworld:id/email_et").click()
    d.send_keys("2421712196@qq.com", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/password_et").click()
    d.send_keys("123456", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/login_btn").click()

    # 切换至个人中心，退出登录
    d.xpath(
        '//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
    # 上拉展示：退出登录按钮
    d.drag(42, 2000,42, 0,1)
    d(resourceId="com.zjiec.sellingworld:id/loginout_btn").click()

    # 邮箱重置密码
    time.sleep(2)
    d(resourceId="com.zjiec.sellingworld:id/sign_email_tv").click()
    time.sleep(2)
    d(resourceId="com.zjiec.sellingworld:id/email_et").click()
    d.send_keys("2421712196@qq.com", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/get_email_code_btn").click()
    # d(resourceId="com.zjiec.sellingworld:id/email_code_et").click()
    d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/email_code_et"]').click()
    d.send_keys("363636", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/password_et").click()
    d.send_keys("123456", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/signup_btn").click()

    # 切换至个人中心，退出登录
    d.xpath(
        '//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
    # 上拉展示：退出登录按钮
    d.drag(42, 2000,42, 0,1)
    d(resourceId="com.zjiec.sellingworld:id/loginout_btn").click()

    # 快捷登录-手机号登录
    d(resourceId="com.zjiec.sellingworld:id/other_login_img").click()
    d(resourceId="com.zjiec.sellingworld:id/login_mobile_btv").click()
    d(resourceId="com.zjiec.sellingworld:id/mobile_phone_et_by_pw").click()
    d.send_keys("18856213801", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/password_et").click()
    d.send_keys("123456", clear=True)
    d(resourceId="com.zjiec.sellingworld:id/login_btn").click()

    # 切换至个人中心，退出登录
    d.xpath(
        '//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
    # 上拉展示：退出登录按钮
    d.drag(42, 2000, 42, 0, 1)
    d.xpath(
        '//*[@resource-id="com.zjiec.sellingworld:id/nested_scrollview"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
    d(resourceId="com.zjiec.sellingworld:id/loginout_btn").click()
    #切换至中文再次进入app
    d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/language_tv"]').click()
    d.xpath('//*[@text="中文"]').click()
    d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/mobile_phone_et"]').click()
    d.send_keys("18856213801", clear=True)
    d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/get_sms_code_btn"]').click()
    d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/sms_code_et"]').click()
    d.send_keys("363636", clear=True)
    d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/login_btn"]').click()





except:
    print('账号密码错误')

#点击登录按钮
# d(resourceId="com.zjiec.sellingworld:id/login_btn").click()
print('--------------001 登录ok----------------')
#判断页面是否有完善信息弹窗，没有pass
try:
    em = d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tv_cancel"]')
    em.click()
except:
    pass
#点击首页banner(如果第一张没有点击到，就点击第二张）
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/banner"]/android.support.v4.view.ViewPager[1]/android.widget.ImageView[1]').click(timeout=30)
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/banner"]/android.support.v4.view.ViewPager[1]/android.widget.ImageView[1]').click()
time.sleep(5)
d(resourceId="com.zjiec.sellingworld:id/webview_close_btn").click()


# if True:
#     d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/banner"]/android.support.v4.view.ViewPager[1]/android.widget.ImageView[1]').click()
#     d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/webview_back_btn"]').click()
# elif:
#     d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/banner"]/android.support.v4.view.ViewPager[1]/android.widget.ImageView[2]').click()
#     d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/webview_back_btn"]').click()
# elif condion3:
#     d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/banner"]/android.support.v4.view.ViewPager[1]/android.widget.ImageView[3]').click()
#     d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/webview_back_btn"]').click()
# else:
#     d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/banner"]/android.support.v4.view.ViewPager[1]/android.widget.ImageView[4]').click()
#     d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/webview_back_btn"]').click()


#点击要闻，进入列表
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tv1"]').click()
time.sleep(2)
d.xpath('//android.widget.ViewFlipper/android.widget.LinearLayout[1]').click()
time.sleep(2)
#切换要闻的type
d.xpath('//*[@text="资讯"]').click()
time.sleep(2)
#关闭页面
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/webview_back_btn"]').click()
#点击海关数据
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/recycler_view"]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
#点击关闭按钮
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/webview_close_btn"]').click()
#海外采购信息
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/iv_bg"]').click()
time.sleep(2)
#返回上级
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/back_btn"]').click()
#全球纺织网
try:
    d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/iv_banner1"]').click()

    time.sleep(2)
    d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/webview_back_btn"]').click()
except:
    pass
#返回上级
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/webview_back_btn"]').click()
#向上滑动页面
d.drag(42, 2000,42, 0,1)
time.sleep(2)
#点击翻译按钮
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/recycler_view"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]').click()
d(resourceId="com.zjiec.sellingworld:id/iv_translate").click()
time.sleep(2)
#点击评论按钮
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/recycler_view"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[3]').click()
d(resourceId="com.zjiec.sellingworld:id/tv_comment").click()
#输入评论内容,并点击发送
time.sleep(2)
d.send_keys("hello", clear=True)
time.sleep(2)
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/comment_send_tv"]').click()
time.sleep(2)
#动态进行点赞\
d(resourceId="com.zjiec.sellingworld:id/tv_like").click()
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/recycler_view"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[4]').click()

time.sleep(2)
#进入个人信息页面
d(resourceId="com.zjiec.sellingworld:id/iv_avatar").click()
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/recycler_view"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
time.sleep(2)
#返回上级页面
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/visible_back_btn"]').click()
#向下滑动让其出现顶部4个类目
d.drag(219, 338,48, 1789,0.1)
#切换服务资源
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tv_source"]').click()
#切换交易市场
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tv_market"]').click()
#切换商务导航
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tv_web"]').click()
#关闭商务导航
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/webview_close_btn"]').click()
print('------------002  首页ok-------------')
#进入联系人页面--新的朋友
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/new_contact_rl"]').click()
#搜索服务端的联系人数据（“18856”）·
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/search_tv"]').click()
d.send_keys("15999", clear=True)
time.sleep(2)
#点击进入个人中心
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/contact_listview"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').click()
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/visible_back_btn"]').click(timeout=15)
time.sleep(2)
d(resourceId="com.zjiec.sellingworld:id/visible_back_btn").click()
time.sleep(2)
#返回至添加通讯录联系人并进入
d(resourceId="com.zjiec.sellingworld:id/left_back_btn").click()
time.sleep(2)
d.xpath('//*[@text="邀请手机通讯录联系人"]').click()
time.sleep(5)
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/visible_back_btn"]').click()
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/left_back_btn"]').click()
d(resourceId="com.zjiec.sellingworld:id/back_btn").click()

#返回上级页面，进入微信联系人--返回
# d.xpath('//*[@resource-id="com.tencent.mm:id/lc"]').click()
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/back_btn"]').click()
d(text="邀请微信联系人").click()
# d(resourceId="com.tencent.mm:id/lc").click()
d(resourceId="com.tencent.mm:id/m0").click()
d(resourceId="com.zjiec.sellingworld:id/back_btn").click()
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/back_btn"]').click()
#进入用户个人中心
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/contact_listview"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]').click()
#分享该用户给好友
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/visible_share_img_btn"]').click()
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/gridView"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/recent_contacts_listview"]/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/navigation_right_tv"]').click()
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/visible_back_btn"]').click()
# # d(resourceId="com.zjiec.sellingworld:id/back_btn").click()#过会删除
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/recent_contacts_listview"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
d(resourceId="com.zjiec.sellingworld:id/navigation_right_tv").click()
time.sleep(3)
# d(resourceId="com.zjiec.sellingworld:id/visible_back_btn").click()
d(resourceId="com.zjiec.sellingworld:id/visible_back_btn").click()
#点击群聊
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/group_chat_rl"]').click()
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/left_back_btn"]').click()
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tag_hint"]').click()
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/back_btn"]').click()
print('--------------003  联系人ok-----------------')

#点击底部中间+号，进入快捷页面
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
#点击发动态按钮
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/send_dynamic_btn"]/android.widget.ImageView[1]').click()
d(resourceId="com.zjiec.sellingworld:id/back_btn").click()
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
#点击扫一扫
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/saoyisao_btn"]/android.widget.ImageView[1]').click()
d(resourceId="com.zjiec.sellingworld:id/back_btn").click()
#点击匹配商友
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/groupFindFriend"]/android.widget.ImageView[1]').click()
d(resourceId="com.zjiec.sellingworld:id/back_btn").click()

#点击交易信息
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/releaseBazaar"]/android.widget.ImageView[1]').click()
d(resourceId="com.zjiec.sellingworld:id/navigation_right_tv").click()
d(text="未通过").click()
time.sleep(2)
d(resourceId="com.zjiec.sellingworld:id/back_btn").click()
time.sleep(2)
d(resourceId="com.zjiec.sellingworld:id/back_btn").click()
time.sleep(2)
print('--------------004  底部快捷键ok--------------')
#切换至消息页面
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
#进入系统消息页面
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
d(resourceId="com.zjiec.sellingworld:id/msg_title_tv").click()
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/system_msg_list"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/system_msg_list"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[3]').click()
# d(resourceId="com.zjiec.sellingworld:id/back_btn").click()
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/back_btn"]').click()
# d(resourceId="com.zjiec.sellingworld:id/visible_back_btn").click()
d(resourceId="com.zjiec.sellingworld:id/back_btn").click()
# //*[@resource-id="com.zjiec.sellingworld:id/visible_back_btn"]
# d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/visible_back_btn"]').click()
# d(resourceId="com.zjiec.sellingworld:id/back_btn").click()
#向上滑动页面
d.drag(42, 1878,42, 150,1)
d(resourceId="com.zjiec.sellingworld:id/back_btn").click()
time.sleep(2)
d.drag(42, 1878,42, 150,1)
d(resourceId="com.zjiec.sellingworld:id/custom_dialog_text_view", text="删除该聊天").click()
print('---------------005  消息ok-----------------')
#进入我的页面
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/tabs"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
#进入基本信息并修改
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/edit_basicinfo_ly"]').click()
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/nickname_tv"]').click()
d.send_keys("Jack", clear=True)
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/navigation_right_tv"]').click()
time.sleep(2)
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/back_btn"]').click()

#向上滑动页面
d.drag(42, 2080,42, 0,1)
d.drag(42, 2080,42, 0,1)
#点击退出登录
d.xpath('//*[@resource-id="com.zjiec.sellingworld:id/loginout_btn"]').click()


d.service('uiautomator').stop()
print('----------- over ------------')
print('THANKS')
print('byes')
