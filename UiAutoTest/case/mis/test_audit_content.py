import pytest

from page.mis.audit_conten_page import AuditContentProxy
from page.mis.home_page import HomeProxy
from page.mis.login_page import LoginProxy
from utils import UtilsDriver


@pytest.mark.run(order=1002)
class TestAuditContent:
    def setup_class(self):
        # 实例化首页面和登录页面、审核页面的业务类
        # self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()
        self.audit_content_proxy = AuditContentProxy()
        # self.login_proxy.login("testid", "testpwd123")

    def teardown_class(self):
        UtilsDriver.quit_mis_driver()

    def test_audit_content(self):
        self.home_proxy.go_audit_page()  # 跳转到审核页面
        self.audit_content_proxy.audit_content("test-2020-11-30", "待审核", "2020-12-30 12:00:00")
        assert "test-2020-11-30" in self.audit_content_proxy.confirm_result("审核通过")
