# encoding:utf-8
import unittest
from tests.ovc1024.demo_fisrstpage import FirstPage
from selenium import webdriver
import json
import time

class TestCase_FirstPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.first_page = FirstPage(self.driver)
        self.first_page.open()

    def test_register_bt_Case01(self):
        ele_register_pst = self.driver.find_element_by_xpath(u"//nav/div/div[3]/a[2]")
        ele_register_pst.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)

        exp_result1 = u"注册_用户_OVC1024"
        act_result1 = self.driver.title
        self.assertEqual(exp_result1,act_result1)

    def test_register_Case02(self):
        ele_register_pst = self.driver.find_element_by_xpath(u"//nav/div/div[3]/a[2]")
        ele_register_pst.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(10)

        mem_register = {
            "email": u"947012@qq.com",
            "password": u"123456",
            "cpassword": u"123456",
            "username": u"ychenyyy"
        }
        self.first_page.register(mem_register)
        ele_register_pst1 = self.driver.find_element_by_id(u"comm-submit")
        ele_register_pst1.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        exp_result2 = "http://47.92.220.226:8000/bbs2/"
        act_result2 = self.driver.current_url
        self.assertEqual(exp_result2, act_result2)
    def test_login_in_Case03(self):
        ele_login = self.driver.find_element_by_xpath(u"//nav/div/div[3]/a[1]")
        ele_login.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        ele_email_input = self.driver.find_element_by_xpath(u"//input[@name='email']")
        ele_password_input = self.driver.find_element_by_name(u"pwd")
        ele_email_input.send_keys(u"947072@qq.com")
        ele_password_input.send_keys(u"123456")

        # 单选：记住我
        ele_login_in_bt = self.driver.find_element_by_name(u"cktime")
        ele_login_in_bt.click()

        ele_login_in = self.driver.find_element_by_id(u"comm-submit")
        ele_login_in.click()
        time.sleep(4)
        exp_result3 = u"http://47.92.220.226:8000/bbs2/"
        act_result3 = self.driver.current_url
        self.assertEqual(exp_result3, act_result3)

    def test_click_Case04(self):
        ele_shouye_cli = self.driver.find_element_by_xpath(u"//nav/div/div[1]/ul/li[1]/a")
        ele_shouye_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result4 = "http://47.92.220.226:8000/bbs2/"
        act_result4 = self.driver.current_url
        self.assertEqual(exp_result4, act_result4)
    def test_click_Case05(self):
        ele_SAAS_cli = self.driver.find_element_by_xpath(u"//nav/div/div[1]/ul/li[2]/a")
        ele_SAAS_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result5 = "https://www.thinksaas.cn/"
        act_result5 = self.driver.current_url
        self.assertEqual(exp_result5, act_result5)
    def test_click_Case06(self):
        ele_pay_cli = self.driver.find_element_by_xpath(u"//nav/div/div[1]/ul/li[3]/a")
        ele_pay_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result6 = "https://www.thinksaas.cn/service/down/"
        act_result6 = self.driver.current_url
        self.assertEqual(exp_result6, act_result6)
    def test_click_Case07(self):
        ele_search_cli = self.driver.find_element_by_xpath(u"//nav/div/div[2]/a")
        ele_search_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result7 = u"搜索_OVC1024"
        act_result7 = self.driver.title
        self.assertEqual(exp_result7, act_result7)

    def test_click_lan01_Case08(self):
        ele_shouye1_cli = self.driver.find_element_by_xpath(u"//body/div[1]/div/a[1]")
        ele_shouye1_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result8 = "http://47.92.220.226:8000/bbs2/"
        act_result8 = self.driver.current_url
        self.assertEqual(exp_result8, act_result8)
    def test_click_lan01_Case09(self):
        ele_xiaozu_cli = self.driver.find_element_by_xpath(u"//body/div[1]/div/a[2]")
        ele_xiaozu_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result9 = "http://47.92.220.226:8000/bbs2/index.php?app=group"
        act_result9 = self.driver.current_url
        print(act_result9)
        print(type(act_result9))
        self.assertEqual(exp_result9, act_result9)
    def test_click_lan01_Case10(self):
        ele_wenzhang_cli = self.driver.find_element_by_xpath(u"//body/div[1]/div/a[3]")
        ele_wenzhang_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result10 = u"文章_OVC1024"
        act_result10 = self.driver.title
        self.assertEqual(exp_result10, act_result10)
    def test_click_lan01_Case11(self):
        ele_xiangce_cli = self.driver.find_element_by_xpath(u"//body/div[1]/div/a[4]")
        ele_xiangce_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result11 = u"相册_OVC1024"
        act_result11 = self.driver.title
        self.assertEqual(exp_result11, act_result11)
    def test_click_lan01_Case12(self):
        ele_laodao_cli = self.driver.find_element_by_xpath(u"//body/div[1]/div/a[5]")
        ele_laodao_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result12 = u"唠叨_OVC1024"
        act_result12 = self.driver.title
        self.assertEqual(exp_result12, act_result12)
    def test_click_lan01_Case13(self):
        ele_yonghu_cli = self.driver.find_element_by_xpath(u"//body/div[1]/div/a[6]")
        ele_yonghu_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result13 = u"用户_OVC1024"
        act_result13 = self.driver.title
        self.assertEqual(exp_result13, act_result13)
    def test_click_lan01_Case14(self):
        ele_shousuo_cli = self.driver.find_element_by_xpath(u"//body/div[1]/div/a[7]")
        ele_shousuo_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result14 = u"搜索_OVC1024"
        act_result14 = self.driver.title
        self.assertEqual(exp_result14, act_result14)
    def test_click_lan01_Case15(self):
        ele_tongcheng_cli = self.driver.find_element_by_xpath(u"//body/div[1]/div/a[8]")
        ele_tongcheng_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result15 = u"登录_用户_OVC1024"
        act_result15 = self.driver.title
        self.assertEqual(exp_result15, act_result15)
    def test_click_lan01_Case16(self):
        ele_shequ_cli = self.driver.find_element_by_xpath(u"//body/div[1]/div/a[9]")
        ele_shequ_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1.5)
        exp_result16 = u"登录_用户_OVC1024"
        act_result16 = self.driver.title
        self.assertEqual(exp_result16, act_result16)

    def test_click_img_Case17(self):
        ele_img1_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[1]/div/div/a/div")
        ele_img1_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        exp_result17 = u"https://www.thinksaas.cn/"
        act_result17 = self.driver.current_url
        self.assertEqual(exp_result17, act_result17)

    def test_click_lan02_Case18(self):
        ele_ASad1_cli = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div/div/div[1]/a")
        ele_ASad1_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        exp_result18 = u"http://47.92.220.226:8000/bbs2/"
        act_result18 = self.driver.current_url
        self.assertEqual(exp_result18, act_result18)
    def test_click_lan02_Case19(self):
        ele_ASad2_cli = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div/div/div[2]/a")
        ele_ASad2_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        exp_result19 = u"https://www.thinksaas.cn/"
        act_result19 = self.driver.current_url
        self.assertEqual(exp_result19, act_result19)
    def test_click_lan02_Case20(self):
        ele_ASad3_cli = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div/div/div[3]/a")
        ele_ASad3_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        exp_result20 = u"http://47.92.220.226:8000/bbs2/"
        act_result20 = self.driver.current_url
        self.assertEqual(exp_result20, act_result20)
    def test_click_lan02_Case21(self):
        ele_ASad4_cli = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div/div/div[4]/a")
        ele_ASad4_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        exp_result21 = u"https://www.thinksaas.cn/"
        act_result21 = self.driver.current_url
        self.assertEqual(exp_result21, act_result21)


    def test_login_in_shouye_lan04_Case24(self):
        user_benren = {
            "email":u"947072@qq.com",
            "password":u"123456"
        }
        self.first_page.login_in(user_benren)
        ele_login_bt = self.driver.find_element_by_xpath(u"//div[3]/div[3]/div[2]/div[1]/div/div/form/button")
        ele_login_bt.click()

        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        exp_result24 = u"http://47.92.220.226:8000/bbs2/"
        act_result24 = self.driver.current_url
        self.assertEqual(exp_result24, act_result24)


    def test_click_lan03_Case22(self):
        ele_qiandao_ychen_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/a")
        ele_qiandao_ychen_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        exp_result22 = u"ychen_用户_OVC1024"
        act_result22 = self.driver.title
        self.assertEqual(exp_result22, act_result22)
    def test_click_lan03_Case23(self):
        ele_qiandao_ychen_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/div/a")
        ele_qiandao_ychen_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        exp_result23 = u"ychen_用户_OVC1024"
        act_result23 = self.driver.title
        self.assertEqual(exp_result23, act_result23)


    def test_click_lan05_Case34(self):
        ele_gengduo_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[1]/div[3]/div[1]/small/a")
        ele_gengduo_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        exp_result34 = "http://47.92.220.226:8000/bbs2/index.php?app=group&ac=tags"
        act_result34 = self.driver.current_url
        self.assertEqual(exp_result34, act_result34)
    def test_click_lan05_Case35(self):
        ele_biaoqian_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[1]/div[3]/div[2]/a[2]")
        ele_biaoqian_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        exp_result35 = "http://47.92.220.226:8000/bbs2/index.php?app=group&ac=tag&id=%E5%8D%A4%E8%9B%8B"
        act_result35 = self.driver.current_url
        self.assertEqual(exp_result35, act_result35)

    def test_click_lan06_Case36(self):
        ele_fandaoshi_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[1]/div[4]/div[2]/div/ul/li[1]/div[1]/a")
        ele_fandaoshi_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        exp_result36 = "http://47.92.220.226:8000/bbs2/index.php?app=user&ac=space&id=10"
        act_result36 = self.driver.current_url
        self.assertEqual(exp_result36, act_result36)
    def test_click_lan06_Case37(self):
        ele_fandaoshi_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[1]/div[4]/div[2]/div/ul/li[1]/div[2]/div[1]/a")
        ele_fandaoshi_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        exp_result37 = "http://47.92.220.226:8000/bbs2/index.php?app=group&ac=topic&id=5"
        act_result37 = self.driver.current_url
        self.assertEqual(exp_result37, act_result37)
    def test_click_lan06_Case38(self):
        ele_fandaoshi_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[1]/div[4]/div[2]/div/ul/li[1]/div[2]/div[3]/span[1]/a")
        ele_fandaoshi_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        exp_result38 = "http://47.92.220.226:8000/bbs2/index.php?app=group&ac=show&id=41"
        act_result38 = self.driver.current_url
        self.assertEqual(exp_result38, act_result38)
    def test_click_lan06_Case39(self):
        ele_fandaoshi_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[1]/div[4]/div[2]/div/ul/li[1]/div[2]/div[3]/span[2]/a")
        ele_fandaoshi_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        exp_result39 = "http://47.92.220.226:8000/bbs2/index.php?app=user&ac=space&id=10"
        act_result39 = self.driver.current_url
        self.assertEqual(exp_result39, act_result39)


    def test_click_lan07_Case40(self):
        user_benren = {
            "email": u"947072@qq.com",
            "password": u"123456"
        }
        self.first_page.login_in(user_benren)
        ele_login_bt = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[2]/div[1]/div/div/form/button")
        ele_login_bt.click()

        ele_content_input = self.driver.find_element_by_name(u"content")

        ele_content_input.send_keys(u"haode")
        ele_fasong_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[1]/form/input[2]")
        ele_fasong_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        exp_result40 = u"haode_唠叨_OVC1024"
        act_result40 = self.driver.title
        self.assertEqual(exp_result40, act_result40)

    def test_click_lan06_Case41(self):
        ele_ychen_img_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[3]/ul/li[1]/span[1]/a")
        ele_ychen_img_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        exp_result41 = u"ychen_用户_OVC1024"
        act_result41 = self.driver.title
        self.assertEqual(exp_result41, act_result41)
    def test_click_lan06_Case42(self):
        ele_ychen_mingzi_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[3]/ul/li[1]/span[2]/span[1]/a")
        ele_ychen_mingzi_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        exp_result42 = u"ychen_用户_OVC1024"
        act_result42 = self.driver.title
        self.assertEqual(exp_result42, act_result42)
    def test_click_lan06_Case43(self):
        ele_ychen_haode_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[3]/ul/li[1]/span[2]/span[3]/a")
        ele_ychen_haode_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        exp_result43 = u"haode_唠叨_OVC1024"
        act_result43 = self.driver.title
        self.assertEqual(exp_result43, act_result43)

    def test_click_lan07_xiaozu_Case44(self):
        ele_pyh_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[2]/div[3]/div[2]/div/ul/li[1]/a")
        ele_pyh_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        exp_result44 = "http://47.92.220.226:8000/bbs2/index.php?app=group&ac=show&id=41"
        act_result44 = self.driver.current_url
        self.assertEqual(exp_result44, act_result44)

    def test_click_lan08_wenzhang_Case45(self):
        ele_rd24d14_cli = self.driver.find_element_by_xpath(u"//div[3]/div[3]/div[2]/div[4]/div[2]/div/ul/li[1]/a")
        ele_rd24d14_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        exp_result45 = u"rd24d14_文章_OVC1024"
        act_result45 = self.driver.title
        self.assertEqual(exp_result45, act_result45)

    def test_click_lan09_huati_Case46(self):
        ele_fandaoshi_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[3]/div[2]/div[5]/div[2]/div/ul/li[1]/a")
        ele_fandaoshi_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        exp_result46 = "http://47.92.220.226:8000/bbs2/index.php?app=group&ac=topic&id=5"
        act_result46 = self.driver.current_url
        self.assertEqual(exp_result46, act_result46)

    def test_click_lan10_xiangce_Case47(self):
        ele_gengduo_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[4]/div[1]/small/a")
        ele_gengduo_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        exp_result47 = "http://47.92.220.226:8000/bbs2/index.php?app=photo"
        act_result47 = self.driver.current_url
        self.assertEqual(exp_result47, act_result47)

    def test_click_lan11_lianjie_Case48(self):
        ele_SAAS_cli = self.driver.find_element_by_xpath(u"//div[3]/div[5]/div[2]/a[1]")
        ele_SAAS_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        exp_result48 = u"https://www.thinksaas.cn/"
        act_result48 = self.driver.current_url
        # print (act_result48)
        self.assertEqual(exp_result48, act_result48)
    def test_click_lan11_lianjie_Case49(self):
        ele_kaiyuan_cli = self.driver.find_element_by_xpath(u"//body/div[3]/div[5]/div[2]/a[2]")
        ele_kaiyuan_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        exp_result49 = "https://www.thinksaas.cn/"
        act_result49 = self.driver.current_url
        self.assertEqual(exp_result49, act_result49)

    def test_click_feedback_Case50(self):
        ele_feedback_cli = self.driver.find_element_by_xpath(u"//body/div[7]/a")
        ele_feedback_cli.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        exp_result50 = "https://www.thinksaas.cn/"
        act_result50 = self.driver.current_url
        self.assertEqual(exp_result50, act_result50)



if __name__ == '__main__':
    unittest.main()
