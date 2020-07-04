import unittest
import HTMLTestRunner
import time
import os

from Tools.scripts.win_add2path import PATH


class TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("this is class")

    def setUp(self):
        print("this is set_up")

    # 跳过当前case
    # @unittest.skip("TestClass")
    def test_01(self):
        print("this is case")

    # @unittest.skip("TestClass")
    def test_02(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        print("this is tear_down")


    @classmethod
    def tearDownClass(cls):
        print("this is tear down class ")

if __name__ == "__main__":
    # # unittest.main()
    # suite = unittest.TestSuite()
    # # suite.addTest(TestClass("test_01"))

    # # unittest.TextTestRunner().run(suite)
    # html_file = "E:/report/report.html"
    # fp = open(html_file, "wb")
    # HTMLTestRunner.HTMLTestRunner(fp).run(suite)
    # fp.close()
    # 实例化测试套件
    suite = unittest.TestSuite()
    # 加载测试用例
    suite.addTest(unittest.TestCase("test_01"))
    suite.addTest(unittest.TestCase("test_02"))
    # 生成测试报告
    # 选择指定时间格式
    time_str = time.strftime('%Y-%m-%d%H%M%S', time.localtime(time.time()))
    # 定义测试报告存放路径和报告名称
    Report = os.path.join(
        PATH('E:/testing_code/code/SmartSiteTestScript/report/test_report') + time_str + '.html')

    with open(Report, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                               verbosity=2,
                                               title='XXXX自动化测试报告',
                                               description='执行人：覃能达')
    runner.run(suite)

# 关闭测试报告
# f.close()