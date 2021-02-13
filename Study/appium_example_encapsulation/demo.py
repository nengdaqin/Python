# 引入 appium
from appium import webdriver

# 设置 capability(启动选项)
desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '11',
    'appPackage': 'com.trnovels.vip.apps',
    'appActivity': 'cn.trtech.muggua.read.ui.activity.SplashActivity',
    # 'noReset': True
}

# 远程启动 appium 的 WebDriver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
