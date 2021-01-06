# 清除输入框值
from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait


def main():
    browser_driver = webdriver.Chrome()
    browser_driver.get('https://www.baidu.com')
    browser_driver.find_element_by_id('kw').send_keys('Selenium')
    time.sleep(3)
    browser_driver.find_element_by_id('kw').clear()


    time.sleep(5)
    browser_driver.quit()


if __name__ == '__main__':
    main()