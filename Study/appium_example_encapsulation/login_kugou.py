from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

def get_driver():
    desired_caps = {}
    # 系统
    desired_caps["platformName"] = "Android"
    # 平台版本
    desired_caps["platformVersion"] = "7.1"
    # 设备号
    desired_caps["deviceName"] = "WTKDU16716002118"
    # 包名
    desired_caps["appPackage"] = "com.kugou.android"
    # 启动名/界面名
    desired_caps["appActivity"] = ".app.splash.SplashActivity"

    # desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps["autoGrantPermissions"] = True # 自动获取权限

    # 连接appium服务器
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver

# 定义全局变量driver
driver = get_driver()

# 获取权限
def get_permission():
    agree_button = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(
        "com.kugou.android:id/l25"))
    agree_button.click()

    # 授权
    grant_button = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(
        "com.kugou.android:id/gek"))
    grant_button.click()

    # 存储权限
    save_agree_button = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(
        "com.android.packageinstaller:id/permission_allow_button"))
    # save_agree_button.click()

    # 电话权限
    phone_agree_button = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(
        "com.android.packageinstaller:id/permission_allow_button"))
    # phone_agree_button.click()
# get_permission()
sleep(10)

# 获取屏幕分辨率
def get_size():
    size = driver.get_window_size([])
    x = size["width"]
    y = size["height"]
    return x, y

# 向左滑动
def swipe_left():
    x1 = get_size()[0] * 0.9
    y1 = get_size()[1] * 0.5
    x = get_size()[0] * 0.1
    driver.swipe(x1, y1, x, y1)
# swipe_left()

# 向右滑动
def swipe_right():
    x1 = get_size()[0] / 10
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10 * 9
    driver.swipe(x1, y1, x, y1)
# swipe_right()

# 向上滑动
def swipe_up():
    x = get_size()[0] * 0.5
    y = get_size()[1] * 0.9
    y1 = get_size()[1] * 0.1
    driver.swipe(x, y, x, y1)
# swipe_up()

# 向下滑动
def swipe_down():
    x = get_size()[0] * 0.5
    y = get_size()[1] * 0.9
    y1 = get_size()[1] * 0.1
    driver.swipe(x, y1, x, y)
# swipe_down()

def swipe_on(direction):
    if direction == "up":
        swipe_up()
    elif direction == "down":
        swipe_down()
    elif direction == "left":
        swipe_left()
    else:
        swipe_right()

def login_mode():
    # 其它登录方式
    # other_button = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(
        # "com.kugou.android:id/fzs"))

    other_button = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(
        "com.kugou.android:id/uv"))
    # print(len(other_button))
    other_button.click()



for i in range(5):
    swipe_on("left")


sleep(5)
driver.quit()