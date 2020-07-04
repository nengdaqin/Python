import os
import HTMLTestRunner
from Tools.scripts.win_add2path import PATH
from appium import webdriver
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait

driver = None


class TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {



        }
        desired_caps["platformName"] =  "Android"
        # desired_caps[x  # 获取toast
        desired_caps["platformVersion"] = "7.1"
        desired_caps["deviceName"] = "127.0.0.1:21503"
        desired_caps["appPackage"] = "ycyh.com.driver"
        desired_caps["appActivity"] = ".activity.MainActivity"
        desired_caps['noReset'] = True  # 启动时不重新安装app
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps["autoGrantPermissions"] = True  # 自动获取权限
        desired_caps["chromeOptions"] = {"androidProcess": "com.tencent.mm:appbrand0"}

        # 连接appium服务器
        global driver
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def test01(self):
        WebDriverWait(driver, 30, 0.5).until(lambda x: x.find_element_by_id
        ("ycyh.com.driver:id/no_car_join")).click()

    time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass
    def tearDown(self):
        global driver



if __name__ == '__main__':
    # unittest.main(verbosity=2)

    suite = unittest.TestSuite()
    # 加载测试用例
    suite.addTest(unittest.TestCase("test01"))
    # 生成测试报告
    # 选择指定时间格式
    time_str = time.strftime('%Y-%m-%d%H%M%S', time.localtime(time.time()))
    # 定义测试报告存放路径和报告名称
    Report = os.path.join(
        PATH('E:/report/report') + time_str + '.html')

    with open(Report, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                               verbosity=2,
                                               title='XXXX自动化测试报告',
                                               description='执行人：覃能达')
    runner.run(suite)
