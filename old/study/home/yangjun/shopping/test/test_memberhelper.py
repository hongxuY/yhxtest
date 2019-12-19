import unittest

from yangjun.shopping.rembers import MemberHelper

class TestMemberHelper(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        print("1,Steup test class")

    @classmethod
    def tearDownClass(cls):
        print("2,Tear Down test class")

    def setUp(self):
        print("3,Set up test case")

    def tearDown(self):
        print("4,Tear Down test case")

    def test_case01_getdefalutdisc(self):
        print("5")
        tel = '1423'
        act_disc = MemberHelper.get_rember_discount(tel)
        exp_disc = 1

        self.assertEqual(exp_disc,act_disc)


    def test_case01_getdefalutdisc(self):
        print("6")
        tel = '18812345672'
        act_disc = MemberHelper.get_rember_discount(tel)
        exp_disc = 0.9

        self.assertEqual(exp_disc,act_disc)


if __name__ == '__main__':
    unittest.main()
