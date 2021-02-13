# 审核文章页面对象
import time

from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle

# 对象库层
from utils import choice_info, UtilsDriver


class AuditContentPage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章标题
        self.title = By.CSS_SELECTOR, '[placeholder="请输入: 文章名称"]'
        # 状态选择下拉框
        self.status_select = By.CSS_SELECTOR, '[placeholder="请选择状态"]'
        # 结束时间
        self.end_time = By.CSS_SELECTOR, '[placeholder="选择结束时间"]'
        # 查询按钮
        self.query_btn = By.CSS_SELECTOR, ".find"
        # 通过按钮
        self.pass_btn = By.XPATH, "//*[@class='el-table__body']/tbody/tr/td[8]/div/button[2]"
        # 确定按钮
        self.confirm_btn = By.CSS_SELECTOR, ".el-button--primary"
        # 查询结果的文章名称
        self.content_name = By.XPATH, "//*[@class='el-table__body']/tbody/tr/td[2]/div"

    # 定位文章标题
    def find_title(self):
        return self.get_element(self.title)

    # 定位选择状态
    def find_status_select(self):
        return self.get_element(self.status_select)

    # 定位结束时间
    def find_end_time(self):
        return self.get_element(self.end_time)

    # 定位查询按钮
    def find_query_btn(self):
        return self.get_element(self.query_btn)

    # 定位通过按钮
    def find_pass_btn(self):
        return self.get_element(self.pass_btn)

    # 定位确定按钮
    def find_confirm_btn(self):
        return self.get_element(self.confirm_btn)

    # 定位到 查询结果之后的第一个文章名称
    def find_content_name(self):
        return self.get_element(self.content_name)


# 操作层
class AuditContentHandle(BaseHandle):
    def __init__(self):
        self.audit_content_page = AuditContentPage()
        self.driver = UtilsDriver.get_mis_driver()

    # 输入文章标题
    def input_title(self, title):
        self.input_text(self.audit_content_page.find_title(), title)

    # 选择状态
    def choice_status(self, status):
        choice_info(self.driver, self.audit_content_page.find_status_select(), status)

    # 输入结束时间
    def input_end_time(self, end_time):
        self.input_text(self.audit_content_page.find_end_time(), end_time)

    # 点击查询按钮
    def click_query_btn(self):
        self.audit_content_page.find_query_btn().click()

    # 点击 通过按钮
    def click_pass_btn(self):
        self.audit_content_page.find_pass_btn().click()

    # 点击 确定 按钮
    def click_confirm_btn(self):
        self.audit_content_page.find_confirm_btn().click()

    # 获取查询结果的第一个文章名称
    def get_content_name(self):
        return self.audit_content_page.find_content_name().text


# 业务层
class AuditContentProxy:
    def __init__(self):
        self.audit_content_handle = AuditContentHandle()

    # 文章审核
    def audit_content(self, title, status, end_time):
        # 输入文章标题
        self.audit_content_handle.input_title(title)
        # 选择状态
        self.audit_content_handle.choice_status(status)
        # 输入结束时间
        self.audit_content_handle.input_end_time(end_time)
        # 点击 查询按钮
        self.audit_content_handle.click_query_btn()
        time.sleep(1)
        # 点击 通过 按钮
        self.audit_content_handle.click_pass_btn()
        time.sleep(1)
        # 点击 确定按钮
        self.audit_content_handle.click_confirm_btn()

    # 确定审核通过的结果
    def confirm_result(self, status):
        self.audit_content_handle.choice_status(status)  # 更改状态
        time.sleep(1)
        self.audit_content_handle.click_query_btn()  # 点击查询按钮
        time.sleep(1)
        return self.audit_content_handle.get_content_name()
