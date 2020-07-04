# coding = utf-8


import HTMLTestRunner
import os
import time
import unittest

from Tools.scripts.win_add2path import PATH
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



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

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(5)
WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_id
("com.huawei.systemmanager:id/optimize_button")).click()


