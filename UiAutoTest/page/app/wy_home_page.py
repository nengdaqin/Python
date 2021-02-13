# 首页面对象
from selenium.webdriver.common.by import By

from base.app.base_page import BasePage, BaseHandle


# 对象库层
class WyHomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 我的 页签
        self.my_page = By.XPATH, "//*[@text='我']"

    # 查找我的页签
    def find_my_page(self):
        return self.get_element(self.my_page)


# 操作层
class WyHomeHandle(BaseHandle):
    def __init__(self):
        self.wy_home_page = WyHomePage()

    # 点击 我的 页签
    def click_my_page(self):
        self.wy_home_page.find_my_page().click()


# 业务层
class WyHomeProxy:
    def __init__(self):
        self.wy_home_handle = WyHomeHandle()

    # 跳转到我的页面
    def go_my_page(self):
        self.wy_home_handle.click_my_page()
