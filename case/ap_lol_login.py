from appium import webdriver
from time import sleep

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
desired_caps["appPackage"] = "com.tencent.qt.qtl"
# 启动名/界面名
desired_caps["appActivity"] = ".activity.main.LauncherActivity"

desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 连接appium服务器
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

#

# 利用坐标点击
# TouchAction(driver).tap(x=400, y=800, count=1).perform()  # count--表示点击的次数
# driver.find_element_by_id("")

agree_button = WebDriverWait(driver, 6, 1).until(lambda x: x.
find_element_by_id("com.tencent.qt.qtl:id/img_privacy_selector"))
agree_button.click()

# sleep(3)
# 点击"QQ登录"
QQ_login_button = WebDriverWait(driver, 3, 1).until(lambda x: x.
find_element_by_xpath("//*[@text='QQ登录']"))
QQ_login_button.click()

# 输入QQ账号密码
Input_box = WebDriverWait(driver, 3, 1).until(lambda x: x.
find_element_by_id("u")).send_keys("782284295")
WebDriverWait(driver, 3, 1).until(lambda x: x.
find_element_by_id("p")).send_keys("QND782284295")

# 登录
login_button = WebDriverWait(driver, 3, 1).until(lambda x: x.
find_element_by_id("go"))
login_button.click()


sleep(30)
driver.quit()