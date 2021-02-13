# 登录 页面
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from base.app.base_page import BasePage, BaseHandle
from utils import UtilsDriver


class WyLoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 账号名输入框
        self.username = By.ID, "com.netease.newsreader.activity:id/ph"
        # 密码输入框
        self.password = By.ID, 'com.netease.newsreader.activity:id/pn'
        # 登录按钮
        self.login_btn = By.ID, "com.netease.newsreader.activity:id/pp"

    # 查找账号输入框
    def find_username(self):
        return self.get_element(self.username)

    # 查找密码输入框
    def find_password(self):
        return self.get_element(self.password)

    # 查找登录按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)


# 操作层
class WyLoginHandle(BaseHandle):
    def __init__(self):
        self.wy_login_page = WyLoginPage()

    # 输入账号名
    def input_username(self, username):
        self.input_text(self.wy_login_page.find_username(), username)
        TouchAction(UtilsDriver.get_app_driver()).tap(x=524, y=493).perform()

    # 输入密码
    def input_password(self, password):
        self.input_text(self.wy_login_page.find_password(), password)

    # 点击登录按钮
    def click_login_btn(self):
        self.wy_login_page.find_login_btn().click()


# 业务层
class WyLoginProxy:
    def __init__(self):
        self.wy_login_handle = WyLoginHandle()

    # 登录
    def login(self, username, password):
        # 输入用户名
        self.wy_login_handle.input_username(username)
        # 输入密码
        self.wy_login_handle.input_password(password)
        # 点击登录
        self.wy_login_handle.click_login_btn()
