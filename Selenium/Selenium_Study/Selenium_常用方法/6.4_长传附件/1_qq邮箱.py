from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://mail.qq.com')
element = WebDriverWait(driver, 5, 0.5).until(
           EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/a[1]/span[4]')))
element.click()