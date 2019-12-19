import unittest

from YZX.shop.members import Members

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("1,set up class case")
    @classmethod
    def tearDownClass(cls):
        print ("2.tear down class case")
    def setUp(self):
        print ("3.set up test case")
    def tearDown(self):
        print ("4.tear down test case")
    def test_case01(self):
        tel='18845871680'
        exp_disc=0.9
        act_disc=Members.get_disc_by_tell(tel)
        self.assertEqual(exp_disc, act_disc)
    def test_case02(self):
        tel = '18845095099'
        exp_disc = 0.1
        act_disc = Members.get_disc_by_tell(tel)
        self.assertEqual(exp_disc, act_disc)
if __name__ == '__main__':
    unittest.main()
