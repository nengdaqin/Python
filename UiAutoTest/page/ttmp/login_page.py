# 登面页面对象
import time

from selenium.webdriver.common.by import By

from base.ttmp.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 手机号码输入框
        self.mobile = By.CSS_SELECTOR, "[placeholder='请输入手机号']"
        # 验证码输入框
        self.code = By.CSS_SELECTOR, "[placeholder='验证码']"
        # 登录按钮
        self.login_btn = By.CSS_SELECTOR, ".el-button--primary"

    # 定位手机号码输入框
    def find_mobile(self):
        return self.get_element(self.mobile)

    # 定位验证码输入框
    def find_code(self):
        return self.get_element(self.code)

    # 定位登录按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)


class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 输入手机号码
    def input_mobile(self, mobile):
        self.input_text(self.login_page.find_mobile(), mobile)

    # 输入验证码
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    # 点击登录按钮
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录业务
    def login(self, mobile, code):
        self.login_handle.input_mobile(mobile)
        self.login_handle.input_code(code)
        time.sleep(1)
        self.login_handle.click_login_btn()