import unittest
from selenium import webdriver
from test_ui_msj import config
from test_ui_msj.msj.common import Common
import time

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        cls.driver=webdriver.Firefox()
        cls.url = config.URL
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(2)

    def test_login_by_password(self):
        self.user=config.USER
        self.password=config.PASSWORD
        self.common=Common()
        self.common.login(self.driver,self.user,self.password)

        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
