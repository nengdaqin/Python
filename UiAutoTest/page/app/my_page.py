# 我的  页面
# 对象库层
from base.app.base_page import BasePage, BaseHandle


class MyPage(BasePage):
    def __init__(self):
        super().__init__()
        #  登录之后的用户名称
        # self.user_info =

# 操作层
class MyHandle(BaseHandle):
    pass

# 业务层
class MyProxy:
    pass