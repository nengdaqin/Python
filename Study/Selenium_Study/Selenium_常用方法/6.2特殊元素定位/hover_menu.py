import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def main():
    browser_driver = webdriver.Chrome()
    browser_driver.maximize_window()
    browser_driver.get('https://xdclass.net/')
    time.sleep(2)
    # 定位鼠标到元素上面
    bg_config = browser_driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[1]/ul/li[1]')

    ActionChains(browser_driver).move_to_element(bg_config).perform()
    bg_menu = browser_driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/a[2]')
    time.sleep(2)
    bg_menu.click()
    time.sleep(5)
    browser_driver.quit()

if __name__ == '__main__':
    main()