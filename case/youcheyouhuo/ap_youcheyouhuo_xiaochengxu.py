from appium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.wait import WebDriverWait

class YcYh(unittest.TestSuite):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["automationName"] = "UiAutomation2"  # 获取toast
        desired_caps["platformVersion"] = "7.1"
        desired_caps["deviceName"] = "127.0.0.1:21503"
        desired_caps["appPackage"] = "com.tencent.mm"
        desired_caps["appActivity"] = ".ui.LauncherUI"
        desired_caps['noReset'] = True  # 启动时不重新安装app
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps["autoGrantPermissions"] = True  # 自动获取权限
        desired_caps["chromeOptions"] = {"androidProcess": "com.tencent.mm:appbrand0"}

        # 连接appium服务器
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return driver

    driver = setUpClass()
    def setUp(self):

        sleep(20)
        # driver.quit()

