import pytest

from page.ttmp.home_page import HomeProxy
from page.ttmp.login_page import LoginProxy
from page.ttmp.publish_article_page import PublishArticleProxy
from utils import UtilsDriver

@pytest.mark.run(order=2)
class TestPublishArticle:
    def setup_class(self):
        self.home_proxy =HomeProxy()
        self.login_proxy = LoginProxy()
        self.publish_article_proxy = PublishArticleProxy()
        self.login_proxy.login("13012345678","246810")

    def teardown_class(self):
        UtilsDriver.quit_ttmp_driver()

    def test_publish_article(self):
        self.home_proxy.go_publish_article_page()
        self.publish_article_proxy.publish_article("test-2020-11-30", "test-2020-11-28", "区块链")
        assert "新增文章成功" in self.publish_article_proxy.get_msg_info()