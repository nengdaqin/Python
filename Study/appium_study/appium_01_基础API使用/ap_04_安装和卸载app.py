from appium import webdriver
import time


desired_caps = {"platformName": "Android",
                "platformVersion": "8.0",
                "deviceName": "WTKDU16716002118",
                "appPackage": "com.huawei.camera",
                "appActivity": "com.huawei.camera"}


# 连接appium服务器
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


# 4.安装与卸载应用
# 1.判断应用是否安装
if driver.is_app_installed("com.ss.android.ugc.aweme"):
    # 2.如果已经安装则卸载
    driver.remove_app("com.ss.android.ugc.aweme")
    print("卸载完成")
else:
    # 3.如果没有安装，则安装
    driver.install_app("C:/Users/qnd/Desktop/com.ss.android.ugc.aweme.apk")