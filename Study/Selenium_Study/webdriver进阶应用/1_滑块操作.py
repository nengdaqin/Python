from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get('https://www.ctrip.com/')
driver.find_element_by_xpath('/html/body/div[5]/div/ul[2]/li[2]/a/span').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[6]/div[3]/a[2]').click()
# 获取滑块元素
sour = driver.find_element_by_css_selector('#slideCode > div.cpt-drop-box > div.cpt-drop-btn')
# print(sour.size['width'])
# print(sour.size['height'])
# 获取滑块区域元素
ele = driver.find_element_by_css_selector('#slideCode > div.cpt-drop-box > div.cpt-bg-bar')
# print(ele.size['width'])
# print(ele.size['height'])
# 拖动滑块
ActionChains(driver).drag_and_drop_by_offset(sour, ele.size['width'], -sour.size['height']).perform()
time.sleep(5)
driver.quit()