# 登录后首页面对象
# 对象库层
import time

from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 管理员用户名称
        self.admin_info = By.CSS_SELECTOR, ".user_info>span"
        # 信息管理菜单
        self.info_manage = By.XPATH, "//*[@class='side_bar']/ul/li[3]/a"
        # 内容审核菜单
        self.audit_content = By.XPATH, "//*[@class='side_bar']/ul/li[3]/ul/li[3]/a"

    # 定位到管理员用户名称
    def find_admin_info(self):
        return self.get_element(self.admin_info)

    # 定位信息管理菜单
    def find_info_manage(self):
        return self.get_element(self.info_manage)

    # 定位内容审核菜单
    def find_audit_content(self):
        return self.get_element(self.audit_content)


# 操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    # 获取管理员用户名称
    def get_admin_info(self):
        return self.home_page.find_admin_info().text

    # 点击 信息管理菜单
    def click_info_manage(self):
        self.home_page.find_info_manage().click()

    # 点击 内容审核菜单
    def click_audit_content(self):
        time.sleep(1)
        self.home_page.find_audit_content().click()


# 业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 获取管理员名称信息
    def get_info(self):
        return self.home_handle.get_admin_info()

    # 跳转到审核页面
    def go_audit_page(self):
        self.home_handle.click_info_manage()
        self.home_handle.click_audit_content()