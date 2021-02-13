from appium import webdriver
import time


desired_caps = {"platformName": "Android",
                "platformVersion": "8.0",
                "deviceName": "WTKDU16716002118",
                "appPackage": "com.huawei.camera",
                "appActivity": "com.huawei.camera"}


# 连接appium服务器
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 进入后台n秒，再回到前台
driver.background_app(5)

time.sleep(5)

driver.quit()