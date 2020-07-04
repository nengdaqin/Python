from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


def get_driver():
    desired_caps = {}
    desired_caps["platformName"] = "Android"
    desired_caps["automationName"] = "UiAutomation2"  # 获取toast
    desired_caps["platformVersion"] = "7.1"
    desired_caps["deviceName"] = "127.0.0.1:21503"
    desired_caps["appPackage"] = "cn.com.open.mooc"
    desired_caps["appActivity"] = "com.imooc.component.imoocmain.index.MCMainActivity"
    desired_caps['noReset'] = True  # 启动时不重新安装app
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps["autoGrantPermissions"] = True  # 自动获取权限

    # 连接appium服务器
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver

driver = get_driver()
# def login_
# 切换到登录界面

sleep(5)
driver.quit()
