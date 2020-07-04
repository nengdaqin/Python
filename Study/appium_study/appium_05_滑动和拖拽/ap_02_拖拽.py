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

# 将"设备连接"按钮拖拽到"电池"按钮

# save_button = driver.find_element_by_xpath("//*[(@text='显示')]")
# battery_button = driver.find_element_by_xpath("//*[(@text='设备连接')]")
# driver.drag_and_drop(save_button, battery_button)


start_ele = driver.find_element_by_xpath("//*[contains(@text,'电池')]")
end_ele = driver.find_element_by_xpath("//*[contains(@text,'无线和网络')]")
driver.scroll(start_ele, end_ele)

