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

# 3.关闭当前APP应用
driver.close_app()

time.sleep(5)
# 退出驱动对象
driver.quit()
