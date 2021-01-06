# 向前操作--浏览器工具栏向前操作
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait


def main():
    browser_driver = webdriver.Chrome()
    browser_driver.get('https://www.baidu.com')
    # browser_driver.find_element_by_id('kw').send_keys('python')
    # browser_driver.find_element_by_id('kw').send_keys(Keys.ENTER)
    browser_driver.back()
    time.sleep(3)
    browser_driver.forward()

    time.sleep(10)
    browser_driver.quit()


if __name__ == '__main__':
    main()