from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

def get_driver():
    desired_caps = {}
    desired_caps["platformName"] = "Android"
    desired_caps["automationName"] = "UiAutomation2" # 获取tost
    desired_caps["platformVersion"] = "8.0"
    desired_caps["deviceName"] = "WTKDU16716002118"
    desired_caps["appPackage"] = "cn.com.open.mooc"
    desired_caps["appActivity"] = "com.imooc.component.imoocmain.splash.MCSplashActivity"
    # desired_caps['noReset'] = True  # 启动时重新安装app
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # desired_caps["autoGrantPermissions"] = True  # 自动获取权限

    # 连接appium服务器
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver

# 定义全局变量driver
driver = get_driver()

# 获取权限
def get_permission():
    agree_button = WebDriverWait(driver, 10).until(lambda x: x.
    find_element_by_id("cn.com.open.mooc:id/negativeBtn"))
    agree_button.click()
get_permission()

# 切换账号密码登录界面
def login_switch():

    user_button = WebDriverWait(driver, 10).until(lambda x: x.
    find_element_by_xpath("//*[@text = '账号密码登录']"))
    user_button.click()
login_switch()

# 输入账号密码---层级定位
def login_by_node():
    element = driver.find_element_by_id("cn.com.open.mooc:id/llPassLogin")
    elements = element.find_elements_by_class_name("android.widget.EditText")
    # print(len(elements))
    elements[0].send_keys("13632960678")
    elements[1].send_keys("test123456")
# login_by_node()

# 通过uiautomator的API定位
def login_by_uiautomator():
    # 显式等待
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_android_uiautomator(
        'new UiSelector().text("请输入手机号/邮箱")')).send_keys("13632960678")
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_android_uiautomator(
        'new UiSelector().text("请输入密码")')).send_keys("test123456")

    # driver.find_element_by_android_uiautomator('new UiSelector().text("请输入手机号/邮箱")')\
    #     .send_keys('13632960678')
    # driver.find_element_by_android_uiautomator('new UiSelector().text("请输入密码")')\
    #     .send_keys('test123456')
login_by_uiautomator()

# 通过xpath定位
def login_xpath():
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
        "//*[@text = '请输入手机号/邮箱']")).send_keys("13632960678")
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
        "//*[@text = '请输入密码']")).send_keys("test123456")
# login_xpath()

# 隐藏输入法
driver.wait_activity(driver.hide_keyboard(), 1)

# 点击"登录"按钮
def login_click():
    login_button = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(
        "cn.com.open.mooc:id/login"))
    login_button.click()
login_click()

# # 获取tost元素
def get_tost():
    message = '登录密码错误'
    element_message = '//*[@text=\'{message}\']'.format(message=message)
    print('message：', element_message)
    tost_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(element_message))
    print('tost：', tost_element.text)
# get_toast()



sleep(5)
driver.quit()