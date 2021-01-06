from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait


def main():
    browser_driver = webdriver.Chrome()
    browser_driver.get('https://www.baidu.com')
    WebDriverWait(browser_driver, 5, 0.5).until(lambda x: x.find_element_by_css_selector(
        '#kw')).send_keys("python")

    time.sleep(10)
    browser_driver.quit()


if __name__ == '__main__':
    main()