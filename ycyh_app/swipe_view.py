# coding = utf-8


import HTMLTestRunner
import os
import time
import unittest

from Tools.scripts.win_add2path import PATH
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


driver = None
class SwipeViewYouCheYouHuo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        # desired_caps["automationName"] = "UiAutomation2"  # 获取toast
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

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        global driver
        WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_id("ycyh.com.driver:id/no_car_join")).click()
        time.sleep(3)
        back_button = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_id("ycyh.com.driver:id/back"))
        back_button.click()

    @staticmethod
    def case_suite():
        suite = unittest.TestSuite()
        suite.addTest(SwipeViewYouCheYouHuo("test_01"))
        file_path = r'E\:report\result.html'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        with open(file_path, 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='描述:').run(suite)


if __name__ == '__main__':
    run = SwipeViewYouCheYouHuo()
    run.case_suite()
    with open(Report, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                               verbosity=2,
                                               title='XXXX自动化测试报告',
                                               description='执行人：覃能达')