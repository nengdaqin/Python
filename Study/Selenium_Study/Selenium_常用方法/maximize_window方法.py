# 实现浏览器窗口最大化

from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait


def main():
    browser_driver = webdriver.Chrome()
    browser_driver.get('https://www.baidu.com')
    browser_driver.maximize_window()

    time.sleep(10)
    browser_driver.quit()


if __name__ == '__main__':
    main()