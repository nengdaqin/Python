import driver as driver
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

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

# 点击"声音按钮"
driver.swipe(600, 1600, 600, 1000)
# driver.implicitly_wait(2)
time.sleep(2)
audio_button = driver.find_element_by_xpath("//*[(@text='声音')]")

audio_button.click()
# TouchAction.press(audio_button).wait(2000).release().perform()
# driver.scroll()
time.sleep(10)
driver.quit()