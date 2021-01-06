# webdriver对浏览器的控件不是完全支持，如浏览器右侧滚动条、副文本等，通常借助JavaScript间接操作
# webdriver提供了两个方法：
# 1. execute_script()--为同步执行且执行时间较短，webdriver会等待同步执行的结果，然后执行后续代码
# 2. execute_async_script()--为异步执行且执行时间较长，webdriver不会等待异步执行的代码结果，而是直接执行后续代码
import time
from selenium import webdriver


def main():
    # 实现百度搜索框输入‘selenium’
    browser_driver = webdriver.Chrome()
    browser_driver.maximize_window()
    browser_driver.get('https://www.baidu.com')
    # js = "document.getElementById('kw').value='selenium'"

    # 实现JavaScript代码完成滚动条的操作
    # 设置浏览器窗口大小，目的是让滚动条显示出来
    browser_driver.set_window_size(800, 700)
    browser_driver.find_element_by_id('kw').send_keys('selenium')
    browser_driver.find_element_by_id('su').click()
    js = 'window.scrollTo(100, 300)'
    # js = 'window.scrollTo(0, document.body.scrollHeight)'

    browser_driver.execute_script(js)
    time.sleep(5)
    browser_driver.quit()

if __name__ == '__main__':
    main()


