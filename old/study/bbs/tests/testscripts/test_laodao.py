# encoding:utf-8
import unittest
from selenium import webdriver
from tests.ovc1024.laodaopage import LaoDaoPage
from ddt import ddt, file_data
from tests.ovc1024 import laodao_config


@ddt
class Test_laodao(unittest.TestCase):
    @classmethod
    @file_data("test_laodao.json")
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.laodaopage = LaoDaoPage(cls.driver)
        cls.laodaopage.open()
        cls.laodaopage.denglu(laodao_config.data)
        cls.laodaopage.dengdai()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 点击首页，跳转到首页
    def test_laodao_case001(self):
        self.laodaopage.find_shouye
        exp_result = 'http://47.92.220.226:8000/bbs2/'
        act_result = self.laodaopage.test_return_shouye
        self.assertEqual(exp_result, act_result, "exp_result:=%s act_result:=%s" % (act_result, exp_result))

    #     文本框中输入文字，点击唠叨发送
    def test_laodao_case002(self):
        self.laodaopage.return_laodao
        self.laodaopage.send_laodao
        self.laodaopage.wait
        act_result = self.laodaopage.test_laodao
        exp_result = u'唠叨测试'
        self.assertEqual(exp_result, act_result, "exp_result:=%s act_result:=%s" % (act_result, exp_result))

    # 点击用户头像跳转到用户界面
    def test_touxiang_case003(self):
        self.laodaopage.return_laodao
        self.laodaopage.click_imge
        act_result = self.laodaopage.test_click_imge
        exp_result = u'粉丝'
        self.assertEqual(exp_result, act_result, "exp_result:=%s act_result:=%s" % (act_result, exp_result))

    # 点击“回复”，成功跳转到该唠叨回复页面点击文本框输入要回复的数值，点击回复.成功回复唠叨
    def test_huifu_case004(self):
        self.laodaopage.return_laodao
        self.laodaopage.huifu_massage
        act_result = self.laodaopage.test_huifu
        exp_result = u'UI自动化回复测试成功'
        self.assertEqual(exp_result, act_result, "exp_result:=%s act_result:=%s" % (act_result, exp_result))

    # 点击页面下方数字,成功跳转至点击页面
    def test_tiaozhuanPage_case005(self):
        self.laodaopage.return_laodao
        self.laodaopage.tiaozhuanPage()
        act_result = self.laodaopage.test_tiaozhuan
        exp_result = 'http://47.92.220.226:8000/bbs2/index.php?app=weibo&ac=index&page=2'
        self.assertEqual(exp_result, act_result, "exp_result:=%s act_result:=%s" % (act_result, exp_result))

    # 点击评价能够跳转到评价页面，并能够评价
    def test_pingjia_case006(self):
        self.laodaopage.return_laodao
        self.laodaopage.pingjia
        exp_result = u'UI测试评价成功'
        act_result = self.laodaopage.test_huifu
        self.assertEqual(exp_result, act_result, "exp_result:=%s act_result:=%s" % (act_result, exp_result))

    #     点击用户名，跳转到用户信息界面
    def test_name_case007(self):
        self.laodaopage.return_laodao
        self.laodaopage.click_name()
        act_result = self.laodaopage.test_click_imge
        exp_result = u'粉丝'
        self.assertEqual(exp_result, act_result, "exp_result:=%s act_result:=%s" % (act_result, exp_result))


if __name__ == '__main__':
    unittest.main()
