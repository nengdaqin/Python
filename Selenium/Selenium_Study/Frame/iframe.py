import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
url = 'https://mail.qq.com/'
driver.get(url)
time.sleep(10)

# 切换到iframe
driver.switch_to.frame('login_frame')

WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_id(
    'u')).send_keys('782284295')
WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_xpath(''
    '/html/body/div[1]/div[4]/div/div/div[2]/form/div[2]/div[1]/input')).send_keys('QND782284295.')

WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_xpath(''
    '/html/body/div[1]/div[4]/div/div/div[2]/form/div[4]/a/input')).click()
time.sleep(10)
driver.quit()
print('test complete')