import unittest
from selenium import webdriver
from test_ui_msj import config
from test_ui_msj.msj.common import Common
import time


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.url = config.URL
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_login_by_password(self):
        self.user = config.USER
        self.password = config.PASSWORD
        self.common = Common()
        msg = self.common.login(self.driver, self.user, self.password)

        fail_list = []

        exp_url = 'https://whiot.ihaozhuo.com/msjPage/index.html#/commodity/packagelist'
        exp_title = '码上检管理系统'
        exp_username = config.USER_NAME

        act_url = msg["url"]
        act_title = msg["title"]
        act_username = msg["username"]

        if exp_url != act_url:
            fail_list.append(act_url)

        if exp_title != act_title:
            fail_list.append(act_title)

        if exp_username != act_username:
            fail_list.append(act_username)

        self.assertEqual(len(fail_list), 0, fail_list)


if __name__ == '__main__':
    unittest.main()
