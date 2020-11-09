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
        desired_caps["platformVersion"] = "10"
        desired_caps["deviceName"] = "127.0.0.1:21503"
        desired_caps["appPackage"] = "com.huawei.systemmanager"
        desired_caps["appActivity"] = "com.huawei.systemmanager.mainscreen.MainScreenActivity"
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
        WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_id
        ("com.huawei.systemmanager:id/optimize_button")).click()

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
