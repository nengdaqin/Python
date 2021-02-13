# 发布文章页面
from selenium.webdriver.common.by import By

from base.ttmp.base_page import BasePage, BaseHandle
from utils import UtilsDriver, choice_info


class PublishArticlePage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章标题
        self.title = By.CSS_SELECTOR, "[placeholder='文章名称']"
        # 文章内容
        self.content = By.CSS_SELECTOR, "#tinymce"
        # 封面选择
        self.cover = By.XPATH, "//*[@class='el-radio-group']/label[3]/span"
        # 频道选择
        self.channel = By.CSS_SELECTOR,"[placeholder='请选择']"
        # 发表按钮
        self.publish_btn = By.XPATH, "//*[text()='发表']"
        # 发表成功提示信息
        self.msg = By.CSS_SELECTOR, ".el-message__content"

    # 定位文章标题
    def find_title(self):
        return self.get_element(self.title)

    # 定位文章内容
    def find_content(self):
        return self.get_element(self.content)

    # 定位封面
    def find_cover(self):
        return self.get_element(self.cover)

    # 定位频道
    def find_channel(self):
        return self.get_element(self.channel)

    # 定位发布按钮
    def find_publish_btn(self):
        return self.get_element(self.publish_btn)

    # 定位提示信息
    def find_msg(self):
        return self.get_element(self.msg)


class PublishArticleHandle(BaseHandle):
    def __init__(self):
        self.publish_article_page = PublishArticlePage()
        self.driver = UtilsDriver.get_ttmp_driver()

    # 输入文章标题
    def input_title(self, title):
        self.input_text(self.publish_article_page.find_title(), title)

    # 输入文章内容
    def input_content(self, content):
        # 如果iframe有ID或者是name属性，可以直接通过id和name属性值来进行切换，否则只能通过iframe元素对象来切换。
        self.driver.switch_to.frame("publishTinymce_ifr")
        self.input_text(self.publish_article_page.find_content(), content)
        self.driver.switch_to.default_content()

    # 选择封面
    def choice_cover(self):
        self.publish_article_page.find_cover().click()

    # 选择频道
    def choice_channel(self, channel):
        """
        :param channel: 表示的是传入的频道信息的文本内容
        :return:
        """
        choice_info(self.driver, self.publish_article_page.find_channel(), channel)

    # 点击发布按钮
    def click_publish_btn(self):
        self.publish_article_page.find_publish_btn().click()

    # 获取提示信息
    def get_msg(self):
        return self.publish_article_page.find_msg().text


class PublishArticleProxy:
    def __init__(self):
        self.publish_article_handle = PublishArticleHandle()

    # 发布文章
    def publish_article(self, title, content, channel):
        self.publish_article_handle.input_title(title)  # 输入文章标题
        self.publish_article_handle.input_content(content)  # 输入文章内容
        self.publish_article_handle.choice_cover()   # 选择封面
        self.publish_article_handle.choice_channel(channel)   # 选择频道
        self.publish_article_handle.click_publish_btn()

    # 获取提示信息
    def get_msg_info(self):
        return self.publish_article_handle.get_msg()