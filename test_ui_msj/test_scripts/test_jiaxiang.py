import unittest
from selenium import webdriver
from test_ui_msj import config
from test_ui_msj.msj.common import Common
import time

class MyTestCase(unittest.TestCase):

    test_url='https://whiot.ihaozhuo.com/msjPage/index.html#/commodity/addttemlist'

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.url = config.URL
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        time.sleep(2)
        cls.user = config.USER
        cls.password = config.PASSWORD
        cls.common = Common()
        cls.common.login(cls.driver, cls.user, cls.password)
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    def setUp(self):
        self.driver.get(self.test_url)

    def test_something(self):

        print("aa")




if __name__ == '__main__':
    unittest.main()




