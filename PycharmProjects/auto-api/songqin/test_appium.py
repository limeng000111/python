
'''
[Appium]   appActivity: .ui.SplashActivity
[Appium]   appPackage: com.zjiec.sellingworld
[Appium]   deviceName: RJC5T17527020026
[Appium]   noReset: false
[Appium]   platformName: Android
[Appium]   platformVersion: 8.0.0
[Appium]   resetKeyboard: true
[Appium]   unicodeKeyboard: true
[Appium]   newCommandTimeout: 0
[Appium]   connectHardwareKeyboard: true
'''
from appium import webdriver
class Appium_driver():
    def get_driver(self):
        try:
            self.desired_caps = {}
            # 设备信息
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '8.0.0'
            self.desired_caps['deviceName'] = 'RJC5T17527020026'
            #             # app的信息
            self.desired_caps['appPackage'] = 'com.zjiec.sellingworld'
            self.desired_caps['appActivity'] = '.ui.SplashActivity'
            self.desired_caps['unicodeKeyboard'] = True
            self.desired_caps['resetKeyboard'] = True
            self.desired_caps['automationName'] = 'uiautomator2'

            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

            print('qqqqqqqq')
            return self.driver
        except Exception as e:
            raise e
if __name__ == '__main__':
    t = Appium_driver()
    t.get_driver()


