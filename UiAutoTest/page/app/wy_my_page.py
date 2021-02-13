# 我的 页面
from selenium.webdriver.common.by import By

from base.app.base_page import BasePage, BaseHandle


# 对象库层
class WyMyPage(BasePage):
    def __init__(self):
        super().__init__()
        # 登录按钮
        self.login_btn = By.ID, "com.netease.newsreader.activity:id/a7a"
        # 用户昵称
        self.nick_name = By.ID, "com.netease.newsreader.activity:id/aqq"

    # 查找定位登录按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)

    # 查找用户昵称
    def find_nick_name(self):
        return self.get_element(self.nick_name)


# 操作层
class WyMyHandle(BaseHandle):
    def __init__(self):
        self.wy_my_page = WyMyPage()

    # 点击登录按钮
    def click_login_btn(self):
        self.wy_my_page.find_login_btn().click()

    # 获取用户昵称
    def get_nick_name(self):
        return self.wy_my_page.find_nick_name().text


# 业务层
class WyMyProxy:
    def __init__(self):
        self.wy_my_handle = WyMyHandle()

    # 跳转到登录页面
    def go_login_page(self):
        self.wy_my_handle.click_login_btn()

    # 获取用户昵称
    def get_name(self):
        return self.wy_my_handle.get_nick_name()