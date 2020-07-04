from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import unittest
# 去掉警告
import warnings

from selenium.webdriver.support.wait import WebDriverWait

driver = None

class LolTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        指定设备信息
        """
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "8.0"
        desired_caps["deviceName"] = "WTKDU16716002118"
        desired_caps["appPackage"] = "com.tencent.qt.qtl"
        desired_caps["appActivity"] = ".activity.main.LauncherActivity"
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 打开APP
        global driver
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        warnings.simplefilter("ignore", ResourceWarning)

    def test_Lol(self):
        # 操作元素
        global driver
        # 勾选隐私政策
        agree_button = WebDriverWait(driver, 10, 0.5).until(lambda x: x.
        find_element_by_id("com.tencent.qt.qtl:id/img_privacy_selector"))
        agree_button.click()

    # def login_in(self):
        # 点击"QQ登录"
        QQ_button = WebDriverWait(driver, 3, 0.5).until(lambda x: x.
        find_element_by_xpath("//*[@text='QQ登录']"))
        QQ_button.click()

        # 输入QQ账号密码
        WebDriverWait(driver, 3, 0.5).until(lambda x: x.
        find_element_by_id("u")).send_keys("782284295")

        WebDriverWait(driver, 3, 0.5).until(lambda x: x.
        find_element_by_id("p")).send_keys("QND782284295")

        # 登录
        login_button = WebDriverWait(driver, 3, 1).until(lambda x: x.
        find_element_by_id("go"))
        login_button.click()

        sleep(20)


    @classmethod
    def tearDownClass(cls):

        # 关闭App
        driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)