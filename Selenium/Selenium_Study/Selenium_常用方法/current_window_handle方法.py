# 返回窗口句柄，即标识窗口字符串
from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait


def main():
    browser_driver = webdriver.Chrome()
    browser_driver.get('https://www.baidu.com')
    print(browser_driver.current_window_handle)
    # 获取当前窗口的url
    print(browser_driver.current_url)
    time.sleep(10)
    browser_driver.quit()


if __name__ == '__main__':
    main()