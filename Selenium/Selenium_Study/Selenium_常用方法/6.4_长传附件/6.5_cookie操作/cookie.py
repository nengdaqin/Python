from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://xdclass.net/')
print("before login:")
for cookie_detail in driver.get_cookies():
    print(cookie_detail)
WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div/div/div[1]/div/div[4]/div[1]/span[2]'))).click()
WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/div/div[1]/input'))).send_keys('18377183873')
WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/div/div[2]/input'))).send_keys('test123456')

WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/div/div[3]/button'))).click()
time.sleep(3)
print("after login:")
for cookie_detail in driver.get_cookies():
    print(cookie_detail)

time.sleep(10)
driver.quit()