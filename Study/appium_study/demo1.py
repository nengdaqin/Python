from appium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
# 系统
desired_caps["platformName"] = "Android"
# 平台版本
desired_caps["platformVersion"] = "8.0"
# 设备号
desired_caps["deviceName"] = "WTKDU16716002118"
# 包名
desired_caps["appPackage"] = "com.android.browser"
# 启动名/界面名
desired_caps["appActivity"] = "com.tencent.mtt.MainActivity"
desired_caps['noReset'] = True
# 中文输入允许
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 连接appium服务器
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
sleep(2)
search_button = driver.find_element_by_xpath("//*[contains(@text,'搜索或输入网址')]").send_keys("python")

driver.find_element_by_xpath("//*[contains(@content-desc,'选择搜索引擎')]").click()
sleep(10)


# 退出
driver.quit()
