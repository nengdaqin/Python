from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
import unittest
# 去掉警告
import warnings

from selenium.webdriver.support.wait import WebDriverWait
import HTMLTestRunner

driver = None

class MoocTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        指定设备信息
        """
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "7.0"
        desired_caps["deviceName"] = "WTKDU16716002118"
        desired_caps["appPackage"] = "cn.com.open.mooc"
        desired_caps["appActivity"] = "com.imooc.component.imoocmain.splash.MCSplashActivity"
        # desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 打开APP
        global driver
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        warnings.simplefilter("ignore", ResourceWarning)

    def test_Mooc(self):
        # 操作元素
        global driver
        agree_button = WebDriverWait(driver, 10).until(lambda x: x.
        find_element_by_id("cn.com.open.mooc:id/negativeBtn"))
        agree_button.click()
        # 登录
        user_button = WebDriverWait(driver, 10).until(lambda x: x.
        find_element_by_xpath("//*[@text = '账号密码登录']"))
        user_button.click()


        # # 输入账号密码
        # input_pwd = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
        #     "//*[@text = '请输入手机号/邮箱']")).send_keys("13632960678")
        # WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
        #     "//*[@text = '请输入密码']")).send_keys("test123456")

    # 通过uiautomator的API定位
    def test_login_by_uiautomator(self):
        global driver
        driver.find_element_by_android_uiautomator('new UiSelector().text("请输入手机号/邮箱")') .\
            send_keys('13632960678')
        driver.find_element_by_android_uiautomator('new UiSelector().text("请输入密码")') .\
            send_keys('test123456')

        # 隐藏输入法
        driver.wait_activity(driver.hide_keyboard(), 1)

        # 点击"登录"按钮
        login_button = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("cn.com.open.mooc:id/login"))
        login_button.click()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):

        # 关闭App
        driver.quit()

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestSuite("test_Mooc"))
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # 定义测试报告存放路径和报告名称
    # now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = "./" + now + "_test.html"
    fw = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fw, title='Testing', description=u'用例执行情况')
    runner.run(suite)
    fw.close()