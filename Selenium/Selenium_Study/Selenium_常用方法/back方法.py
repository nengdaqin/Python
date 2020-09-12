# 返回操作--后退
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

    time.sleep(10)
    browser_driver.quit()


if __name__ == '__main__':
    main()