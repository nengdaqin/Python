from appium import webdriver
import time


desired_caps = {"platformName": "Android",
                "platformVersion": "8.0",
                "deviceName": "WTKDU16716002118",
                "appPackage": "com.huawei.camera",
                "appActivity": "com.huawei.camera"}


# 连接appium服务器
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 获取当前包名
print(driver.current_package)
# 获取当前界面名
print(driver.current_activity)