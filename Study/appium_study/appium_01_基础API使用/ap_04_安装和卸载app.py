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
desired_caps["appPackage"] = "com.huawei.camera"
# 启动名/界面名
desired_caps["appActivity"] = "com.huawei.camera"

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