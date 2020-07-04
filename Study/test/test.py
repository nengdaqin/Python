from appium import webdriver
from time import sleep
import pandas
import unittest

driver=None

class BaiduTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #指定设备信息
        device = {}
        device['deviceName']='192.168.120.103:5555'
        device['platformName']='Android'
        device['platformVersion']='9'
        device['appPackage']='com.android.quicksearchbox'
        device['appActivity']='com.android.quicksearchbox.SearchActivity'
        device['noReset'] = True
        device['unicodeKeyboard'] = True
        device['resetKeyboard'] = True
        #打开App
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub",device)

    def testBaidu(self):
        #操作元素
        global driver
        driver.find_element_by_id("com.android.quicksearchbox:id/search_src_text").send_keys("www.baidu.com")
        driver.press_keycode(66)
        sleep(3)
        driver.find_element_by_id("org.chromium.webview_shell:id/url_field").clear()
        driver.find_element_by_id("org.chromium.webview_shell:id/url_field").send_keys("www.baidu.com")
        driver.press_keycode(66)
        sleep(3)
        driver.find_element_by_id("index-kw").click()
        driver.find_element_by_id("index-kw").send_keys("python编程")
        driver.press_keycode(66)
        sleep(3)

    @classmethod
    def tearDownClass(cls):
        #关闭App
        driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)

