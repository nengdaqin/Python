import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

# move_to_element()方法
def main():
    browser_driver = webdriver.Chrome()
    browser_driver.maximize_window()
    browser_driver.get('https://www.baidu.com')
    bg_config = browser_driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
    # 模拟将鼠标悬停在超链接‘设置’处
    ActionChains(browser_driver).move_to_element(bg_config).perform()
    # 鼠标悬停时，定位元素，超链接‘高级搜索’，然后实现单击操作
    browser_driver.find_element_by_link_text('高级搜索').click()
    browser_driver.find_element_by_xpath(
        '').click()

    time.sleep(5)
    browser_driver.quit()

if __name__ == '__main__':
    main()