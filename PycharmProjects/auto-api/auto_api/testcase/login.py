'''
coding:UTF-8
author:limeng
time:2019-12-2
'''
import time
import json
import unittest
import requests
import HTMLTestRunner
import auto_api.log.log as log
import random
from auto_api.mysql.mysql_db import Connect_db
import configparser as cparser
import os
from auto_api.tools.send_email import sendEmail
import time
from tomorrow3 import threads



class Test_Login(unittest.TestCase):
    # 获取配置文件中的token
    # cf = cparser.ConfigParser
    # token = cf.get('user','token')
    #声明全局变量：token
    global token


    def setUp(self) -> None:
        self.url = 'http://api.demobizpal.com/v_3_0_0/user_manage/verifiCodeLogin'
        self.logger = log.logger
        self.Connect_db = Connect_db
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))
        base_dir = base_dir.replace('\\', '/')
        file_path = base_dir + '/mysql/db_config.ini'
        self.logger.info(file_path)
        # print(file_path)
        # logger.INFO(file_path)

        # 初始化获取配置信息的实例
        self.cf = cparser.ConfigParser()
        self.cf.read(file_path)


    def tearDown(self) -> None:
        pass

    # def config(self):
    #     # 获取配置文件信息
    #     base_dir = str(os.path.dirname(os.path.dirname(__file__)))
    #     base_dir = base_dir.replace('\\', '/')
    #     file_path = base_dir + '/mysql/db_config.ini'
    #     self.logger.info(file_path)
    #     # print(file_path)
    #     # logger.INFO(file_path)
    #
    #     # 初始化获取配置信息的实例
    #     cf = cparser.ConfigParser()
    #     cf.read(file_path)
    #     return cf

    #手机验证码登录（已存在的）
    def test_verify_code_login(self):
        mobile = self.cf.get('user','mobile')
        data = {
            'mobile' :mobile,
            'login_type':'12',
            'device_id' : '1a1018970ace7c23bf5',
            'code' : '363636',
            'lang' : 'zh_cn',
            'request_type' : 'ios',
            'countrycode' : '86'
        }
        res = requests.post(url=self.url,data = data)
        #self.logger.info(res)
        result = res.json()
        #self.logger.info(result)
        self.assertEqual(result['status'],200)
        self.assertEqual(result['data']['user_id'],'1569315027')

    #输入不存在的手机号登录（注册）
    def test_sign_in(self):
        #生成随机的手机号
        first = ['137','155','152','153','188','189','156']
        #mobile_phone = random.choice(first) + ''.join(random.choice('0123456789') for i in range(8))
        mobile_phone = random.choice(first)+"".join(random.choice("0123456789") for i in range(8))
        data = {
            'mobile': mobile_phone,
            'login_type': '12',
            'device_id': '1a1018970ace7c23bf5',
            'code': '363636',
            'lang': 'zh_cn',
            'request_type': 'ios',
            'countrycode': '86'
        }
        #self.logger.info(mobile_phone)
        url = 'http://api.demobizpal.com/v_3_0_0/user_manage/verifiCodeLogin'
        res = requests.post(url=url, data=data)
       # self.logger.info(res)
        result = res.json()
        # print(result['data']['token'])
        self.logger.info('----001----%s'%result)
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['msg'],'produce_reg intergral+ 4')
        # globals()['token'] = result['data']['token']

    #短信发送接口
    def test_sms_send(self):
        url = 'http://api.demobizpal.com/v_3_0_0/sms/sendSms'
        first = ['137', '155', '152', '153', '188', '189', '156']
        # mobile_phone = random.choice(first) + ''.join(random.choice('0123456789') for i in range(8))
        mobile_phone = random.choice(first) + "".join(random.choice("0123456789") for i in range(8))
        data = {
            'countrycode':'86',
            'mobile':mobile_phone,
            'msg_type':'8',
            'request_type':'ios',
            'lang':'zh-cn'
        }
        res = requests.post(url=url,data=data)
        result = res.json()
        #self.logger.info(result)
        self.assertEqual(result['msg'],'短信发送成功')

    #邮箱注册
    def test_email_sign_in(self):
        #随机生成邮箱
        #邮箱后缀
        Suffix_list = ['@qq.com','@sina.cn','@gmail.com','@hotmail.com','@yahoo.com']
        format = random.choice(Suffix_list)
        number = '012345678qwertyuiopASDFGHJKLMNVCXZ'
        random_test = random.randint(4,10)
        a = "".join(random.choice(number) for i in range(random_test))
        email = a + format
        #self.logger.info('随机生成的email %s'%email)
        # self.logger.info(email_test)
        #注册地址的url
        url = 'http://api.demobizpal.com/v_3_0_0/user_manage/registered'
        data = {
            'email': email,
            'device_id':'160a3797c84bb710184',
            'code': '363636',
            'request_type': 'ios',
            'lang': 'zh-cn'
        }
        #睡眠2s，避免重复生成主主键
        res = requests.post(url=url,data=data)
        result = res.json()
        #self.logger.info('邮箱注册返回信息%s' % result)
        self.assertEqual(result['status'],200)
        self.assertEqual(result['msg'], '注册成功 积分+ 4')
        #核对数据库数据

        sql ="SELECT * from bizpal.cn_user_info WHERE user_email = '%s'"% email
            # self.logger.info('--------sql-------',sql)
        result_data = self.Connect_db().query_db(sql)
            # self.logger.info('sql运行成功')
            # self.logger.info('-----sql_data----',result_data)
            # self.logger.info('------lalalal----------',result_data[0]['user_email'])
        self.assertEqual(result_data[0]['user_email'],email)
        # self.logger.info('-----------user_email------------',result_data[0]['user_email'])


    #完善信息接口
    def test_Perfect_information(self):


        url = 'http://api.demobizpal.com/v_3_0_0/user_manage/Perfect_information'
        data = {
            'user_nickname' : 'test',
            'request_type' : 'android',
            'is_pwd' : 1,
            'token' : Test_friends().get_token(),
            #'token' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjbnNlbGxlcnMiLCJpYXQiOjE1NzUzNTE4OTcsImV4cCI6MTU3NTk1NjY5NywidXNlcl9pZCI6MTU3NTM1MTg5Nywic2hvcF9pZCI6MH0.UvXXvM1OVqqPxsgJP738Cdu1ABcC_hajcCzgD13c0R0',
            'user_pwd' : 'e10adc3949ba59abbe56e057f20f883e',
            'user_country_code' : 'CN',
            'lang' : 'zh-cn'
        }
        res = requests.post(url=url,data=data)
        result = res.json()
        self.logger.info('------information------%s'%result)
        self.assertEqual(result['status'],200)

class Test_first_page(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://api.demobizpal.com/v_3_0_0/user_manage/verifiCodeLogin'
        self.logger = log.logger
        self.Connect_db = Connect_db
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))
        base_dir = base_dir.replace('\\', '/')
        file_path = base_dir + '/mysql/db_config.ini'
        self.logger.info(file_path)
        # print(file_path)
        # logger.INFO(file_path)

        # 初始化获取配置信息的实例
        self.cf = cparser.ConfigParser()
        self.cf.read(file_path)


    def tearDown(self) -> None:
        pass
    #检查banner接口是否正常
    def test_getBanner(self):
        url = 'http://api.demobizpal.com/v_3_0_0/Banner/getBanner'
        data = {
            'type' : 1,
            'token' : Test_friends().get_token(),
            'request_type' : 'android',
            'lang' : 'zh-cn'
        }
        res = requests.post(url=url,data=data)
        result = res.json()
        #self.logger.info(result)
        self.assertEqual(result['status'],200)

    #获取首页新闻列表
    def test_getNewslist(self):
        url = 'http://api.demobizpal.com/v_3_0_0/News/getNewslist'
        data = {
            'page' : 0,
            'token' : Test_friends().get_token(),
            'request_type' : 'android',
            'lang' : 'zh-cn'
        }
        res = requests.post(url=url,data=data)
        result = res.json()
        self.logger.info(result)
        self.assertEqual(result['status'],200)

    #海外采购信息
    def test_getOverseasInfoList(self):
        url = 'http://api.demobizpal.com/v_3_0_0/Overseasinfo/getOverseasInfoList'
        data = {
            'request_type' : 'android',
            'c_o_id' : 'null',
            'page' : 1,
            # 'token' : token,
            'token' : Test_friends().get_token(),
            'lang' : 'zh-cn'
        }
        res = requests.post(url=url,data=data)
        result = res.json()
        self.logger.info(result)
        self.assertEqual(result['status'],200)

    #首页朋友圈
    def test_friends_circle(self):
        url = self.cf.get('app','url') + '/v_3_0_0/friends/getFriendsList'
        token = Test_friends().get_token()
        data = {
            'token' : token,
            'request_type' : 'android',
            'lang' : 'zh-cn',
        }
        res = requests.post(url=url,data=data)
        result = res.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['msg'],'成功')

    #朋友圈点赞
    def test_friends_like(self):
        url = self.cf.get('app', 'url') + '/v_3_0_0/friends_circle/likeFriendsCircle'
        token = Test_friends().get_token()
        data = {
            'token': token,
            'request_type': 'android',
            'lang': 'zh-cn',
            'fc_id' : 'FC_157611314278497307'
        }
        res = requests.post(url=url, data=data)
        result = res.json()
        self.assertEqual(result['status'], 200)
        # self.assertEqual(result['msg'], '点赞 积分+ 1')

    #朋友圈评论
    def test_friends_comment(self):
        url = self.cf.get('app', 'url') + '/v_3_0_0/friends_circle/commentsFriendsCircle'
        token = Test_friends().get_token()
        data = {
            'token': token,
            'request_type': 'android',
            'lang': 'zh-cn',
            'fc_id' : 'FC_157611314278497307',
            'fcc_reveive_user_id':'0',
            'fcc_content':'dhshsh'
        }
        res = requests.post(url=url, data=data)
        result = res.json()
        self.assertEqual(result['status'], 200)
        # self.assertEqual(result['msg'], '点赞 积分+ 1')

    #转发朋友圈动态---到动态中
    def test_friends_forward(self):
        url = self.cf.get('app', 'url') + '/v_3_0_0/friends_circle/forwardFriendsCircle'
        token = Test_friends().get_token()
        data = {
            'token': token,
            'request_type': 'android',
            'lang': 'zh-cn',
            'fc_id' : 'FC_157611314278497307',
            'fcc_reveive_user_id':'0',
            'fcc_content':'dhshsh',
            'fc_url' : 'https://api.demobizpal.com/v_3_0_0/friends_circle/shareCircle?fc_id=FC_157611314278497307&request_type=android',
            'fc_url_content':'贸人动态',
            'fc_type':'1',
            'fc_is_private':'0',
            'fc_content':'djdjdj',
            'fc_permissions':1,
            'fc_url_img':'http://www.filedemocnsellers.com/image.php/media/20191212/c0bbe1846d09b9e33cd97d1531edd091.jpg',
        }
        res = requests.post(url=url, data=data)
        result = res.json()
        self.assertEqual(result['status'], 200)




#联系人页面接口
class Test_friends(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = log.logger
        self.Connect_db = Connect_db
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))
        base_dir = base_dir.replace('\\', '/')
        file_path = base_dir + '/mysql/db_config.ini'
        self.logger.info(file_path)
        # print(file_path)
        # logger.INFO(file_path)

        # 初始化获取配置信息的实例
        self.cf = cparser.ConfigParser()
        self.cf.read(file_path)
        self.url = self.cf.get('app','url')
        self.mobile = self.cf.get('user','mobile')

    def tearDown(self) -> None:
        pass

    #获取18856213800的token
    def get_token(self):

        data = {
            'mobile': 18856213800,
            'login_type': '12',
            'device_id': '1a1018970ace7c23bf5',
            'code': '363636',
            'lang': 'zh_cn',
            'request_type': 'ios',
            'countrycode': '86'
        }
        self.url = 'http://api.demobizpal.com/v_3_0_0/user_manage/verifiCodeLogin'
        res = requests.post(url=self.url, data=data)
        # self.logger.info(res)
        result = res.json()
        # self.logger.info(result)
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['data']['user_id'], '1569315027')
        # self.logger.info('------------18856213800的token-------%s' % result['data']['token'])
        return result['data']['token']
    #获取联系人列表
    def test_get_friends(self):
        url = self.url+'/v_3_0_0/friends/getFriendsList'
        self.logger.info('--------url-----------%s'%url)
        token = Test_friends().get_token()
        self.logger.info('------此处的token为------%s'%token)
        data = {
            'request_type':'android',
            'lang':'zh-cn',
            'token':token
        }
        res = requests.post(url=url,data=data)
        result = res.json()
        self.logger.info('------联系人列表-----%s'%result)
        self.assertEqual(result['status'],200)

    #获取申请好友列表
    def test_apply_friends(self):
        url = self.url + '/v_3_0_0/friends/friendApplyList'
        token = Test_friends().get_token()
        data = {
            'token' : token,
            'request_type' : 'android',
            'lang' : 'zh-cn'
        }
        res = requests.post(url=url,data=data)
        result = res.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['msg'],'成功')

    #搜索app联系人（服务器）
    def test_search_Friend(self):
        url = self.url + '/v_3_0_0/friends/searchFriend'
        token = Test_friends().get_token()
        data = {
            'token': token,
            'request_type': 'android',
            'lang': 'zh-cn',
            'keyword':'18856'
        }
        res = requests.post(url=url, data=data)
        self.logger.info('----------res-----------%s'%res)
        result = res.json()
        self.logger.info('-----------result-----------%s'%result)
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['msg'], '成功')

    #获取用户的手机联系人通讯录
    def test_Get_ContactList(self):
        url = self.url + '/v_3_0_0/user/getContactList'
        token = Test_friends().get_token()
        data = {
            'token': token,
            'request_type': 'android',
            'lang': 'zh-cn'
        }
        res = requests.post(url=url, data=data)
        result = res.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['msg'], '成功')






if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H_%M_%S")

    file = 'C:/Users/dell/PycharmProjects/auto-api/auto_api/report/' + now + '_testresult.html'
    fp = open(file, 'wb')  # 创建测试报告文件

    suite = unittest.TestSuite()  # 创建测试套件
    suite.addTest(Test_Login('test_verify_code_login'))  # 向测试套件中添加测试用例
    suite.addTest(Test_Login('test_sign_in'))
    suite.addTest(Test_Login('test_sms_send'))
    suite.addTest(Test_Login('test_email_sign_in'))
    suite.addTest(Test_Login('test_Perfect_information'))

    #首页接口
    suite.addTest(Test_first_page('test_getBanner'))
    suite.addTest(Test_first_page('test_getNewslist'))
    suite.addTest(Test_first_page('test_getOverseasInfoList'))
    suite.addTest(Test_first_page('test_friends_circle'))
    suite.addTest(Test_first_page('test_friends_like'))
    suite.addTest(Test_first_page('test_friends_comment'))
    suite.addTest(Test_first_page('test_friends_forward'))

    #联系人页面接口
    suite.addTest(Test_friends('test_get_friends'))
    suite.addTest(Test_friends('test_apply_friends'))
    suite.addTest(Test_friends('test_search_Friend'))
    suite.addTest(Test_friends('test_Get_ContactList'))

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试结果如下：',verbosity=2,)
    runner.run(suite)  # 执行测试
    fp.close()


