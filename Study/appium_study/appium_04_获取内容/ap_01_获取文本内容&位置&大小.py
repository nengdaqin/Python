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

# 获取设置界面(android:id/title)的文本内容
# titles = driver.find_elements_by_id("android:id/title")
# for i in titles:
#     print(i.text)

# 获取元素的位置和大小
setting_button = driver.find_element_by_id("android:id/action_bar_title")
print(setting_button.location)
# 打印X轴的位置
print(setting_button.location["x"])
print(setting_button.size)

driver.quit()