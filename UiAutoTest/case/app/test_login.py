from page.app.wy_home_page import WyHomeProxy
from page.app.wy_login_page import WyLoginProxy
from page.app.wy_my_page import WyMyProxy
from utils import UtilsDriver


class TestLogin:
    def setup_class(self):
        #实例化登录页面的业务层类
        # self.login_proxy = LoginProxy()
        self.wy_home_proxy = WyHomeProxy()
        self.wy_my_proxy = WyMyProxy()
        self.wy_login_proxy = WyLoginProxy()

    def teardown_class(self):
        UtilsDriver.quit_app_driver()

    def test_login(self):
        # assert self.login_proxy.login("13911111111","246810")
        # 跳转到我的页面
        self.wy_home_proxy.go_my_page()
        # 跳转到登录页面
        self.wy_my_proxy.go_login_page()
        # 登录操作
        self.wy_login_proxy.login("liaohui19850109@163.com","Lion@284728")
        assert "Ferde" in self.wy_my_proxy.get_name()