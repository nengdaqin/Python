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

# 点击"无线和网络"
WLAN_button = driver.find_element_by_xpath("//*[@text='无线和网络']")
TouchAction(driver).tap(WLAN_button).perform()

# 利用坐标点击
TouchAction(driver).tap(x=400, y=800, count=1).perform()  # count--表示点击的次数
time.sleep(30)
driver.quit()