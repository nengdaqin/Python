import time

from selenium import webdriver
from appium import webdriver as appdriver
from selenium.webdriver.common.by import By


class UtilsDriver:
    ttmp_driver = None  # 自媒体平台驱动
    mis_driver = None  # 后台管理系统驱动
    app_driver = None   # app驱动
    is_mis_driver = True   # 用来判断是否退出mis驱动
    # 定义获取自媒体平台的驱动
    @classmethod
    def get_ttmp_driver(cls):
        if cls.ttmp_driver is None:
            cls.ttmp_driver = webdriver.Chrome()  # 创建浏览器驱动
            # cls.ttmp_driver = webdriver.Firefox()
            cls.ttmp_driver.maximize_window()
            cls.ttmp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.ttmp_driver

    # 定义退出自媒体平台的驱动
    @classmethod
    def quit_ttmp_driver(cls):
        if cls.ttmp_driver is not None:
            cls.get_ttmp_driver().quit()
            cls.ttmp_driver = None    #  如果不置为None后面不会再云创建驱动


    # 定义获取后台管理系统的驱动
    @classmethod
    def get_mis_driver(cls):
        if cls.mis_driver is None:
            cls.mis_driver = webdriver.Chrome()  # 创建浏览器驱动
            cls.mis_driver.maximize_window()
            cls.mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls.mis_driver

    # 定义 退出后台管理系统的驱动
    @classmethod
    def quit_mis_driver(cls):
        if cls.mis_driver is not None and cls.is_mis_driver:
            cls.get_mis_driver().quit()
            cls.mis_driver = None    #  如果不置为None后面不会再去创建驱动

    #  定义获取app的驱动
    @classmethod
    def get_app_driver(cls):
        desired_caps = {"platformName": "Android",  # 平台
                        'platformVersion': '5.1',  # 平台版本
                        'deviceName': '****',  # 设备ID
                        'appPackage': 'com.netease.newsreader.activity',  # app包名
                        'appActivity': 'com.netease.nr.biz.ad.AdActivity',  # app界面名（首次打开的界面名）=
                        'unicodeKeyboard': True,
                        'resetKeyboard': True,
                        'noReset': True
                        }
        if cls.app_driver is None:
            cls.app_driver = appdriver.Remote("http://localhost:4723/wd/hub", desired_caps) # 创建app驱动
        return cls.app_driver

    #  定义退出app驱动
    @classmethod
    def quit_app_driver(cls):
        if cls.app_driver is not None:
            cls.get_app_driver().quit()
            cls.app_driver = None


# 封装一个选择频道的方法
def choice_info(driver, element, channel):
    """
    :param driver:  表示的是驱动
    :param element:  表示的下拉选择框元素对象
    :param channel: 表示的是要选择的频道的文本内容
    :return:
    """
    element_info = By.XPATH, "//*[text()='{}']".format(channel)
    # 点击下拉框元素对象
    element.click()
    time.sleep(1)
    driver.find_element(*element_info).click()


# 封装一个判断元素是否存在的方法
def is_exist_element(driver, element):
    """
    :param driver:  驱动对象
    :param element:  元素定位的信息
    :return:  返回的是True或者False
    """
    try:
        driver.find_element(*element)
        return True
    except Exception as e:
        return False

# 验证
# UtilsDriver.get_ttmp_driver()
# UtilsDriver.quit_ttmp_driver()
#
# UtilsDriver.get_mis_driver()
# UtilsDriver.quit_mis_driver()
#
# UtilsDriver.get_app_driver()
# UtilsDriver.quit_app_driver()