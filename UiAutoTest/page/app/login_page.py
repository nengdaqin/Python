# 登录页面对象

# 对象库层
from selenium.webdriver.common.by import By

from base.app.base_page import BasePage, BaseHandle
from utils import is_exist_element, UtilsDriver


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 手机号输入框
        self.mobile = By.XPATH, "//*[@class='android.widget.EditText' and @index='1']"
        # 验证码输入框
        self.code = By.XPATH, "//*[@class='android.widget.EditText' and @index='2']"
        # 登录按钮
        self.login_btn = By.CLASS_NAME, "android.widget.Button"

    # 查找手机号输入框
    def find_mobile(self):
        return self.get_element(self.mobile)

    # 查找验证码输入框
    def find_code(self):
        return self.get_element(self.code)

    # 查找登录按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)


# 操作层
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

    # 判断手机号码输入框是否存
    def is_mobile_exist(self):
        return is_exist_element(UtilsDriver.get_app_driver(), self.login_page.mobile)

# 业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录操作
    def login(self, mobile, code):
        # 输入手机号码
        self.login_handle.input_mobile(mobile)
        # 输入验证码
        self.login_handle.input_code(code)
        # 点击登录按钮
        self.login_handle.click_login_btn()
        return self.login_handle.is_mobile_exist()