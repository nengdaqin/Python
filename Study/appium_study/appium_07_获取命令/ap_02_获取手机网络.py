from appium import webdriver
import time
from appium.webdriver.connectiontype import ConnectionType

from appium.webdriver.common.touch_action import TouchAction

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

# 获取当前网络
print(driver.network_connection)

# 设置当前网络
driver.set_network_connection(1)
# 判断当前网络
if driver.network_connection == ConnectionType.DATA_ONLY:
    print(1)
else:
    print(0)

time.sleep(10)
driver.quit()