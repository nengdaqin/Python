from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait


def main():
    browser_driver = webdriver.Chrome()
    browser_driver.get('https://www.baidu.com')
    print(browser_driver.find_element_by_link_text('新闻').text)

    time.sleep(10)
    browser_driver.quit()


if __name__ == '__main__':
    main()