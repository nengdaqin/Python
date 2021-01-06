from selenium import webdriver
import time

def main():
    file_path = r"E:\Test_File\WebDriver\Edge\edgedriver_win64\msedgedriver.exe"
    # browser = webdriver.Chrome()
    # browser = webdriver.Ie()
    # browser = webdriver.Firefox()
    browser = webdriver.Edge(file_path)

    browser.get('https://www.baidu.com')
    browser.find_element_by_css_selector("#kw").send_keys("python")
    browser.find_element_by_css_selector("#su").click()
    time.sleep(10)
    browser.quit()

if __name__ == '__main__':
    main()