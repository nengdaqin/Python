from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

def main():
    # chrome_driver = r'F:\python_path\Scripts\chromedriver.exe'  # chromedriver的文件位置
    # IE_driver = r'F:\python_path\Scripts\IEDriverServer.exe'
    # Fire_fox_driver = r'F:\python_path\Scripts\geckodriver.exe'
    # browser = webdriver.Firefox(executable_path=Fire_fox_driver)

    # 不定义浏览器驱动文件路径

    browser = webdriver.Chrome()
    # browser = webdriver.Ie()
    # browser = webdriver.Firefox()

    browser.get('https://www.baidu.com')
    browser.find_element_by_css_selector("input[id='kw']").send_keys("python")

    time.sleep(10)
    browser.quit()

if __name__ == '__main__':
    main()