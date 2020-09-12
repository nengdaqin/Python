# coding = utf-8
import time
import os
import unittest
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class LoginYCYH(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 进入ycyh首页
        # path_browser_driver = r'D:\Chrome\Application\chromedriver.exe'
        # cls.driver = webdriver.Chrome(executable_path=path_browser_driver)
        cls.driver = webdriver.Chrome()
        url = 'http://www.ycyh56.com/'
        cls.driver.get(url)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        print('finsh than 10s：closed chromedriver.exe')
        os.system('tasklist | find "chromedriver.exe"')
        os.system('taskkill -F -PID chromedriver.exe')
        time.sleep(10)

    def setUp(self):
        pass

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        WebDriverWait(self.driver, 3, 1).until(lambda x: x.find_element_by_xpath(
            '//*[@id="nav114"]/div/a/span[1]')).click()
        WebDriverWait(self.driver, 3, 1).until(lambda x: x.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/form/div[2]/div/div[1]/input')).send_keys('123456')
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/form/div[4]/div/div[1]/input').send_keys('abd123')
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/form/div[6]/div/button/span').click()
        time.sleep(10)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginYCYH("test_01"))
    file_path = r"E:\GitHub\Report\Selenium\result.html"
    with open(file_path, "wb") as f:
        HTMLTestRunner.HTMLTestRunner(stream=f,
                                      verbosity=2,
                                      title='xxx自动化测试报告如下',
                                      description='测试人员：xxx').run(suite)
