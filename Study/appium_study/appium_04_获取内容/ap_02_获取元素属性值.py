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

# 连接appium服务器
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 获取id为(android:id/title)的属性值
titles = driver.find_elements_by_id("android:id/title")
for i in titles:
    print(i.get_attribute("enabled"))
    print(i.get_attribute("text"))
    print(i.get_attribute("name"))  #
    print(i.get_attribute("resourceId"))
    print(i.get_attribute("className"))