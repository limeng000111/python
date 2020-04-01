import requests
import json


# url = 'Referer: http://api.demobizpal.com/v_2_0_0//Share/card5'
# data = {
# 'userid':'1555227502',
# 'user_id':'1555227502',
#         'lang':'zh-cn',
# 'from':'singlemessage',
# # }
# class RunSend:
#     def __init__(self,url,method,data=None):
#         self.t = self.run_main(url,method,data)
#
#
#     def send_get(self,url, data):
#         """ 定义send_get函数，用来接收参数，发送get请求 """
#         r = requests.get(url=url, params=data)
#         result = r.json()
#         return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
#
#     def send_post(self,url, data):
#         """ 定义send_post函数，用来接收参数，发送post请求 """
#         r = requests.post(url=url, data=data)
#         result = r.json()
#         return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
#
#     def run_main(self,url,method,data=None):
#
#
#         # if method == 'get':
#         #     res = self.send_get(url,data)
#         # else:
#         #     res = self.send_post(url,data)
#
#         if method == 'GET':
#             res = self.send_get(url, data)
#         else:
#             res = self.send_post(url, data)
#         return res
#
#
# if __name__ == '__main__':
#     # url = 'http://api.demobizpal.com/v_2_0_0/user/getUserInfo'
#     # data = {'request_type': 'android',
#     #         'lang': 'zh-cn',
#     #         'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjbnNlbGxlcnMiLCJpYXQiOjE1NzIzMTM1MDYsImV4cCI6MTU3MjkxODMwNiwidXNlcl9pZCI6IjE1NjkzMTUwMjciLCJzaG9wX2lkIjoiMCJ9.dEjeZM95AYn2vLkdHDnxNrdFC4wSN52RdF6MZmVmWQ8',
#     #         }
#     ru = RunSend(url,'GET',data)
#     print(ru.t)

class RunMain():
    """含有构造器"""
    # def __init__(self, url, method, data=None):
    #     self.t = self.run_main(url, method, data)

    def send_post(self, url, data):
        r = requests.post(url=url, data=data)
        result = r.json()

        return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)

    def send_get(self, url, data):
        r = requests.get(url=url, params=data)
        # print(type(r))
        result = r.json()
        # return result
        return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
        # 利用json.dumps将响应数据进行json格式的编码解析
        # indent=2将输出结果缩进2个字符显示
        # sort_keys=False，输出结果是否按照关键字排序
        # json.dumps 序列化时对中文默认使用的ascii编码，ensure_ascii=False才会输出中文
        # return result

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            r = self.send_get(url, data)
            # print(r)
        else:
            r = self.send_post(url, data)
            # print(r)
        return r

if __name__ == '__main__':
    url = 'http://api.demobizpal.com/v_2_0_0/user/getUserInfo'
    data = {'request_type': 'android',
                'lang': 'zh-cn',
                'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjbnNlbGxlcnMiLCJpYXQiOjE1NzIzMTM1MDYsImV4cCI6MTU3MjkxODMwNiwidXNlcl9pZCI6IjE1NjkzMTUwMjciLCJzaG9wX2lkIjoiMCJ9.dEjeZM95AYn2vLkdHDnxNrdFC4wSN52RdF6MZmVmWQ8',
                }
    run = RunMain()
    run.run_main(url,'POST',data)