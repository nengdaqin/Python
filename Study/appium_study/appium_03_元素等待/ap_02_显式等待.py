from appium import webdriver
import time
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

# 显式等待
back_button = WebDriverWait(driver, 10, 1).until(lambda x: x.
find_element_by_xpath("//*[@content-desc='向上导航']")).click()

# 使用id的方法
# back_button = WebDriverWait(driver, 10, 1).until(lambda x: x.
# find_element_by_id("com.android.settings:id/back"))
# back_button.click()

time.sleep(5)
driver.quit()