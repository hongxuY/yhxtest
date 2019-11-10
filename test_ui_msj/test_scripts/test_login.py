import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        cls.drive=webdriver.Firefox()
        cls.drive.get()


    def test_login(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
