import pytest

from page.mis.home_page import HomeProxy
from page.mis.login_page import LoginProxy
from utils import UtilsDriver


@pytest.mark.run(order=1001)
class TestLogin:
    def setup_class(self):
        # 实例化页面对象的业务层类
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()

    def teardown_class(self):
        UtilsDriver.quit_mis_driver()

    def test_login_success(self):
        self.login_proxy.login("testid", "testpwd123")
        assert "管理员" in self.home_proxy.get_info()