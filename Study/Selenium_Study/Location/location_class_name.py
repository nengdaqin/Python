# coding = utf-8
import time
import os
import unittest
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class LoginMeiTuan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 进入美团首页
        cls.browser_driver = webdriver.Chrome()
        url = 'https://www.baidu.com/'
        cls.browser_driver.get(url)
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        # print('finsh than 10s：closed chromedriver.exe')
        # os.system('tasklist | find "chromedriver.exe"')
        # os.system('taskkill -F -PID chromedriver.exe')
        pass
        time.sleep(10)

    def setUp(self):
        pass

    def tearDown(self):
        self.browser_driver.quit()

    def test_01(self):
        WebDriverWait(self.browser_driver, 5, 0.5).until(lambda x: x.find_element_by_class_name(
            's_ipt')).send_keys("python")

        time.sleep(10)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginMeiTuan("test_01"))
    file_path = r"E:\Python\Report\Selenium\result.html"
    with open(file_path, "wb") as f:
        HTMLTestRunner.HTMLTestRunner(stream=f,
                                      verbosity=2,
                                      title='xxx自动化测试报告如下',
                                      description='测试人员：xxx').run(suite)
