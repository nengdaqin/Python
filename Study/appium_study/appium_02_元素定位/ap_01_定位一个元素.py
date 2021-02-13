from appium import webdriver
import time


desired_caps = {"platformName": "Android",
                "platformVersion": "8.0",
                "deviceName": "WTKDU16716002118",
                "appPackage": "com.android.deskclock",
                "appActivity": ".AlarmsMainActivity"}


# 连接appium服务器
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(5)
# 1.通过id定位设置按钮
setting_button = driver.find_element_by_id("com.android.deskclock:id/alarm_settings_btn").click()

# 2.通过class定位返回按钮
back_button = driver.find_element_by_class_name("android.widget.ImageView").click()

# 3.通过xpath点击新建按钮()
new_button = driver.find_element_by_xpath("//*[(@text='计时器'])")
# new_button = driver.find_element_by_id("com.android.deskclock:id/alarm_new_btn").click()
new_button.click()

time.sleep(5)
driver.quit()