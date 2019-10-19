# coding:utf-8
import unittest
from selenium import webdriver
from tests.ovc1024.tongcheng_page import TongCheng
from tests.ovc1024.register import register_page



class TestTongCheng(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.TongCheng = TongCheng(cls.driver)
        cls.TongCheng.open()
        user = {
            "username": "12345@qq.com",
            "password": "12345"
        }
        cls.TongCheng.login(user)
        cls.TongCheng.go_to_tongcheng()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def test_case01(self):
    #     self.TongCheng.ele_longin.click()
    #     Register_Page=register_page(self.driver)
    #     if_open,error_msg=Register_Page.if_page_open_success()
    #     print "[debug] open:%s"%if_open
    #     print "[debug] msg:%s"%str(error_msg)
    #     # self.assertTrue(if_open,str(error_msg))
    #     self.assertEqual(True,if_open,str(error_msg))


    # #case01_01点击北京下面的加入按钮，结果会进入到北京同城的页面
    # def test_case01_01(self):
    #     self.TongCheng.ele_beijing.click()
    #     time.sleep(4)
    #     act_result = self.TongCheng.ele_beijing_img.get_attribute("alt")
    #     exp_result = (u"北京")
    #     self.assertEqual(act_result, exp_result)
    #
    #case01_02点击武汉下面的加入按钮，结果会进入到武汉同城的页面
    # def test_case01_02(self):
    #     self.TongCheng.ele_wuhan.click()
    #     # time.sleep(4)
    #     act_result = self.TongCheng.ele_wuhan_img.get_attribute("alt")
    #     exp_result = (u"武汉")
    #     self.assertEqual(act_result, exp_result)

    # #case02_01点击退出同城，结果会回到加入同城前的界面
    # def test_case02_01(self):
    #     self.TongCheng.ele_exit_tongcheng.click()
    #     time.sleep(4)
    #     act_result = self.TongCheng.ele_card_header.text
    #     exp_result = u"选择加入同城"
    #     self.assertEqual(act_result, exp_result)

    #case03_01点击用户头像，结果是进入到该用户的首页页面
    def test_case03_01(self):
        exp_result = self.TongCheng.ele_touxiang.get_attribute("alt")
        self.TongCheng.ele_touxiang.click()
        act_result = self.TongCheng.ele_touxiang_souye.get_attribute("alt")
        self.driver.back()
        self.assertEqual(act_result, exp_result)

    #case03_02点击用户名，结果是进入到该用户的首页页面
    def test_case03_02(self):
        exp_result = self.TongCheng.ele_touxiang.get_attribute("alt")
        self.TongCheng.ele_name.click()
        act_result = self.TongCheng.ele_touxiang_souye.get_attribute("alt")
        self.driver.back()
        self.assertEqual(act_result, exp_result)

    #case04_01点击图片，结果是进入到该图片所在相册的页面
    #

    # def test_case04_01(self):
    #     exp_result = self.TongCheng.ele_photo.get_attribute("src")
    #     self.TongCheng.ele_photo.click()
    #     act_result = self.TongCheng.ele_photo1.get_attribute("src")
    #     self.driver.back()
    #     self.assertEqual(act_result, exp_result)

    # case05_01点击发帖人头像，结果是进入到发帖人首页
    def test_case05_01(self):
        exp_result = self.TongCheng.ele_t_phtot.get_attribute("alt")
        self.TongCheng.ele_t_phtot.click()
        act_result = self.TongCheng.ele_touxiang_souye.get_attribute("alt")
        self.driver.back()
        self.assertEqual(act_result, exp_result)

    #case05_02点击发帖人用户名，结果是进入发帖人首页
    #

    # def test_case05_02(self):
    #     exp_result = self.TongCheng.ele_t_phtot.get_attribute("alt")
    #     self.TongCheng.ele_t_name.click()
    #     act_result = self.TongCheng.ele_touxiang_souye.get_attribute("alt")
    #     self.driver.back()
    #     self.assertEqual(act_result, exp_result)

    #case05_03点击帖子标题，结果是进入到帖子内容页面
    def test_case05_03(self):
        exp_result = self.TongCheng.ele_t_title.get_attribute("title")
        self.TongCheng.ele_t_title.click()
        act_result = self.TongCheng.ele_t_title1.text
        self.driver.back()
        self.assertEqual(act_result, exp_result)

    #case05_04点击组名，结果是进入到小组信息页面
    def test_case05_04(self):
        exp_result = self.TongCheng.ele_t_class.text
        self.TongCheng.ele_t_class.click()
        act_result = self.TongCheng.ele_t_class1.text
        self.driver.back()
        self.assertEqual(act_result, exp_result)

    #case05_05点击帖子回复数，结果是进入到该贴子内容页面
    def test_case05_05(self):
        exp_result = self.TongCheng.ele_t_title.get_attribute("title")
        self.TongCheng.ele_t_title.click()
        act_result = self.TongCheng.ele_t_title1.text
        self.driver.back()
        self.assertEqual(act_result, exp_result)

    #case06_01点击唠叨发表者头像，结果是进入到发表者首页
    def test_case06_01(self):
        exp_result = self.TongCheng.ele_l_photo.get_attribute("alt")
        self.TongCheng.ele_l_photo.click()
        act_result = self.TongCheng.ele_touxiang_souye.get_attribute("alt")
        self.driver.back()
        self.assertEqual(act_result, exp_result)

    #case06_02点击唠叨发表者用户名，结果是进入到发表者首页
    def test_case06_02(self):
        exp_result = self.TongCheng.ele_l_photo.get_attribute("alt")
        self.TongCheng.ele_l_name.click()
        act_result = self.TongCheng.ele_touxiang_souye.get_attribute("alt")
        self.driver.back()
        self.assertEqual(act_result, exp_result)

    #case06_03点击唠叨评价，结果是进入到唠叨的发表页面
    def test_case06_03(self):
        exp_result = self.TongCheng.ele_l_laodao.text
        self.TongCheng.ele_l_ping.click()
        act_result = self.TongCheng.ele_l_laodao1.text
        self.driver.back()
        self.assertEqual(act_result, exp_result)

    #case07_01点击文章标题，结果是进入到该文章页面
    def test_case07_01(self):
        exp_result = self.TongCheng.ele_wenzhang.text
        self.TongCheng.ele_wenzhang.click()
        act_result = self.TongCheng.ele_wenzhang1.text
        self.driver.back()
        self.assertEqual(act_result, exp_result)

    #case08_01点击点击全部同城后，结果是进入到全部同城访问页面
    def test_case08_01(self):
        self.TongCheng.ele_all.click()
        act_result = self.TongCheng.ele_al.text
        exp_result = u"全部同城"
        self.driver.back()
        self.assertEqual(act_result, exp_result)


if __name__ == '__main__':
    unittest.main()
