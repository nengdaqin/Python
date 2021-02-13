# 定义对象库层的基类
from selenium.webdriver.support.wait import WebDriverWait

from utils import UtilsDriver


class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_mis_driver()

    # 定义获取元素对象的方法
    def get_element(self, location):
        """
        :param location:  表示的是元素定位的信息
        :return:   返回的是一个元素对象
        """
        wait = WebDriverWait(self.driver, 10)
        return wait.until(lambda x:x.find_element(*location))


# 定义操作层的基类
class BaseHandle:
    # 定义元素输入的方法
    def input_text(self,element, text):
        """
        :param element:  表示的元素对象
        :param text: 表示的是输入的内容
        :return:
        """
        element.clear()
        element.send_keys(text)