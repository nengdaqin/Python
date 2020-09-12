# 刷新页面，类似F5

from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait


def main():
    browser_driver = webdriver.Chrome()
    browser_driver.get('https://www.baidu.com')
    browser_driver.refresh()

    time.sleep(5)
    browser_driver.quit()


if __name__ == '__main__':
    main()