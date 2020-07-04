from appium import webdriver
import time

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

# --等待操作(.wait(ms)方法)
TouchAction(driver).press(x=500, y=1000).release().wait(3000).press(x=300, y=400).release().perform()
time.sleep(3)
# 长按
TouchAction(driver).press(x=400, y=700).wait(3000).perform()

time.sleep(20)
driver.quit()