import pytest

from page.ttmp.home_page import HomeProxy
from page.ttmp.login_page import LoginProxy
from utils import UtilsDriver

@pytest.mark.run(order=1)
class TestLogin:
    def setup_class(self):
        # 实例化业层类
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()

    def teardown_class(self):
        UtilsDriver.quit_ttmp_driver()

    def test_login_success(self):
        self.login_proxy.login("13012345678","246810")
        assert "test123" in self.home_proxy.get_user_info()