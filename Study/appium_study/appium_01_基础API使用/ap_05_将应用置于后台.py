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

# 进入后台n秒，再回到前台
driver.background_app(5)

time.sleep(5)

driver.quit()