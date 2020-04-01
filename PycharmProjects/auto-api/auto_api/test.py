import  requests
import random

def test_sign_in():
    first = ['137', '155', '152', '153', '188', '189', '156']
    # mobile_phone = random.choice(first) + ''.join(random.choice('0123456789') for i in range(8))
    mobile_phone = random.choice(first) + "".join(random.choice("0123456789") for i in range(8))
    data = {
        'mobile': mobile_phone,
        'login_type': '12',
        'device_id': '1a1018970ace7c23bf5',
        'code': '363636',
        'lang': 'zh_cn',
        'request_type': 'ios',
        'countrycode': '86'
    }
    # self.logger.info(mobile_phone)
    url = 'http://api.demobizpal.com/v_3_0_0/user_manage/verifiCodeLogin'
    res = requests.post(url=url, data=data)
    # self.logger.info(res)
    result = res.json()
    print(result)
test_sign_in()