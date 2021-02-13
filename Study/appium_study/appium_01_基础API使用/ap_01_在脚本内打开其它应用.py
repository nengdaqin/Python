from appium import webdriver
import time

desired_caps = {"platformName": "Android",
                "platformVersion": "8.0",
                "deviceName": "WTKDU16716002118",
                "appPackage": "com.huawei.camera",
                "appActivity": "com.huawei.camera"}

# 连接appium服务器
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 等待时间
time.sleep(5)

# 1.跳转到相机应用
driver.start_activity("com.ss.android.ugc.aweme", ".splash.SplashActivity")

driver.quit()
