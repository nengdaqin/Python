# 获取页面的title

from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait


def main():
    browser_driver = webdriver.Chrome()
    browser_driver.get('https://www.baidu.com')
    print(browser_driver.title)

    time.sleep(5)
    browser_driver.quit()

if __name__ == '__main__':
    main()