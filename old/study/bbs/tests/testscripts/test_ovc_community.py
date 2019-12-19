#encoding:utf-8

import unittest
from selenium import webdriver
from tests.ovc1024.ovc_community_page import LocationPage
import time
import json


class MyTestCase(unittest.TestCase):
    @classmethod

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.location_page = LocationPage(self.driver)
        self.location_page.open()

    def tearDown(self):
        self.driver.quit()

    #登录
    def test_register_case01(self):
        register_data = {
            'email':u'123@qq.com',
            'password':u'123'
        }
        self.location_page.register(register_data)
        time.sleep(5)
        self.location_page.ele_aptest.click()

        act = self.driver.current_url
        exp = "http://47.92.220.226:8000/bbs2/index.php?app=my"
        self.assertEqual(exp,act)

    #我的相册
    def test_register_case02(self):
        register_data = {
            'email': u'123@qq.com',
            'password': u'123'
        }
        self.location_page.register(register_data)
        time.sleep(5)
        self.location_page.ele_aptest.click()

        self.location_page.ele_myphototest.click()

        act = self.driver.current_url
        exp = "http://47.92.220.226:8000/bbs2/index.php?app=photo&ac=my"
        self.assertEqual(exp,act)

    #我的同城
    def test_register_case03(self):
        register_data = {
            'email': u'123@qq.com',
            'password': u'123'
        }
        self.location_page.register(register_data)
        time.sleep(5)
        self.location_page.ele_aptest.click()

        self.location_page.ele_mycitytest.click()

        act = self.driver.current_url
        exp = "http://47.92.220.226:8000/bbs2/index.php?app=location&ac=my"
        self.assertEqual(exp, act)

    #账户设置基本信息,设置用户名，设置签名，设置自我介绍，修改设置，返回
    def test_register_case04(self):
        register_data = {
            'email': u'123@qq.com',
            'password': u'123'
        }
        self.location_page.register(register_data)
        time.sleep(5)
        self.location_page.ele_aptest.click()

        self.location_page.ele_installtest.click()
        self.location_page.ele_basictest.click()
        self.location_page.instert_username.send_keys("jack")
        self.location_page.instert_sign.send_keys(u"取次花丛懒回顾，半缘修道半缘君")
        self.location_page.instert_introduce.send_keys(u"大家好，我是Jack")
        self.location_page.instert_install.click()
        self.location_page.instert_return.click()

        act = self.driver.current_url
        exp = "http://47.92.220.226:8000/bbs2/index.php?app=my&ac=setting&ts=base"
        self.assertEqual(exp, act)

    #账户设置修改密码，旧密码，新密码，输入新密码，提交修改，返回
    def test_register_case05(self):
        register_data = {
            'email': u'123@qq.com',
            'password': u'123'
        }
        self.location_page.register(register_data)
        time.sleep(5)
        self.location_page.ele_aptest.click()

        self.location_page.ele_installtest.click()
        self.location_page.ele_password.click()
        self.location_page.instert_password.send_keys(u"123")
        self.location_page.instert_newpassword.send_keys(u"123")
        self.location_page.instert_rwpassword.send_keys(u"123")
        self.location_page.instert_inspassword.click()
        self.location_page.instert_return3.click()

        act = self.driver.current_url
        exp = "http://47.92.220.226:8000/bbs2/index.php?app=my&ac=setting&ts=pwd"
        self.assertEqual(exp,act)

    #账户设置修改账号，新Email账号，提交修改，返回
    def test_register_case06(self):
        register_data = {
            'email': u'123@qq.com',
            'password': u'123'
        }
        self.location_page.register(register_data)
        time.sleep(5)
        self.location_page.ele_aptest.click()

        self.location_page.ele_installtest.click()
        self.location_page.ele_account_test.click()
        self.location_page.instert_newemail.send_keys(u"123@qq.com")
        self.location_page.instert_insemail.click()
        self.location_page.instert_return4.click()

        act = self.driver.current_url
        exp = "http://47.92.220.226:8000/bbs2/index.php?app=my&ac=setting&ts=email"
        self.assertEqual(exp,act)

    def test_register_case07(self):
        register_data = {
            'email': u'123@qq.com',
            'password': u'123'
        }
        self.location_page.register(register_data)
        time.sleep(5)
        self.location_page.ele_aptest.click()

        self.location_page.ele_installtest.click()
        self.location_page.ele_label.click()
        self.location_page.instert_inslabel.send_keys(u"你好你好你好")
        self.location_page.instert_add.click()

        act = self.driver.current_url
        exp = "http://47.92.220.226:8000/bbs2/index.php?app=my&ac=setting&ts=tag"
        self.assertEqual(exp,act)




    # def test_regiter_case02(self):



    # def test_something(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
