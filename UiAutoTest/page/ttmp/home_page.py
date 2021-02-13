# 登录首页对象
import time

from selenium.webdriver.common.by import By

from base.ttmp.base_page import BasePage, BaseHandle


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户名昵称
        self.nick = By.CSS_SELECTOR, ".user-name"
        # 内容管理菜单
        self.content_manage = By.XPATH, "//*[@class='sidebar-el-menu el-menu']/div[2]/li/div"
        # 发布文章菜单
        self.publish_article = By.XPATH, "//*[@class='sidebar-el-menu el-menu']/div[2]/li/ul/li"

    # 定位用户名的昵称
    def find_nick(self):
        return self.get_element(self.nick)

    # 定位内容管理菜单
    def find_content_manage(self):
        return self.get_element(self.content_manage)

    # 定位发布文章菜单
    def find_publish_article(self):
        return self.get_element(self.publish_article)


class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    # 获取用户昵称
    def get_nick(self):
        return self.home_page.find_nick().text

    # 点击 内容管理菜单
    def click_content_manage(self):
        time.sleep(1)
        self.home_page.find_content_manage().click()

    # 点击发布文章菜单
    def click_publish_article(self):
        time.sleep(1)
        self.home_page.find_publish_article().click()


class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 获取用户昵称
    def get_user_info(self):
        return self.home_handle.get_nick()   # 通过reture返回对应的用户昵称给用例来断言

    # 跳转到发布文章页面
    def go_publish_article_page(self):
        self.home_handle.click_content_manage()
        self.home_handle.click_publish_article()