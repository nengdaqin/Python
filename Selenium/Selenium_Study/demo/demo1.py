from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

def main():
    chrome_driver = r'D:\Chrome\Application\chromedriver.exe'  # chromedriver的文件位置
    browser = webdriver.Chrome(executable_path=chrome_driver)
    browser.get('https://www.baidu.com')
    time.sleep(5)
    browser.quit()

if __name__ == '__main__':
    main()