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

# 通过id的形式，获取android:id/title的元素，并打印其内容
# titles = driver.find_elements_by_id("android:id/title")
# print(titles)
# print(len(titles))
# for title in titles:
#     print(title.text)

# 通过class的形式，获取android.widget.TextView的元素，并打印其内容
# text_views = driver.find_elements_by_class_name("android.widget.TextView")
# print(len(text_views))
# for title in text_views:
#     print(title.text)

# 通过xpath的形式，获取"设"的元素，并打印其内容
# settings = driver.find_elements_by_xpath("//*[contains(@text,'设')]")
# for setting in settings:
#     print(setting.text)