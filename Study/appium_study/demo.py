from appium import webdriver
import time

desired_caps = {}
# 系统
desired_caps["platformName"] = "Android"
# 平台版本
desired_caps["platformVersion"] = "8.0"
# 设备号
desired_caps["deviceName"] = "WTKDU16716002118"
# 包名
desired_caps["appPackage"] = "com.android.settings"
# 启动名/界面名
desired_caps["appActivity"] = ".HWSettings"

# 中文输入允许
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 连接appium服务器
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

driver.find_element_by_xpath("//*[contains(@text,'电池')]").click()

# 等待时间
time.sleep(6)
# 退出
driver.quit()
