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
desired_caps["appPackage"] = "com.android.settings"
# 启动名/界面名
desired_caps["appActivity"] = ".HWSettings"

# 连接appium服务器
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 发送键到设备
# 按音量+两次再返回，最后锁屏
# driver.press_keycode(24)
# driver.press_keycode(24)
# driver.press_keycode(4)
# driver.press_keycode(26)
# 打开通知栏
driver.open_notifications()
# 关闭通知栏
time.sleep(5)
driver.press_keycode(4)
driver.quit()