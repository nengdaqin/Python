# 登录页面对象
from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle

# 对象库层
from utils import UtilsDriver


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户名输入框
        self.username = By.NAME, "username"
        # 密码输入框
        self.password = By.NAME, "password"
        # 登录按钮
        self.login_btn = By.CSS_SELECTOR, ".input_sub"

    # 定位用户名输入框
    def find_username(self):
        return self.get_element(self.username)

    # 定位密码输入框
    def find_password(self):
        return self.get_element(self.password)

    # 定位登录按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)


# 操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)

    # 点击登录按钮
    def click_login_btn(self):
        js = "document.getElementById('inp1').removeAttribute('disabled')"
        UtilsDriver.get_mis_driver().execute_script(js)
        self.login_page.find_login_btn().click()


# 业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录
    def login(self, username, password):
        # 输入用户名
        self.login_handle.input_username(username)
        # 输入密码
        self.login_handle.input_password(password)
        # 点击登录按钮
        self.login_handle.click_login_btn()
