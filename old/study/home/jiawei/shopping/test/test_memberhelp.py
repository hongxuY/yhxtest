# encoding:utf-8
import unittest
from jiawei.shopping.members import MemberHelp


class Testmemberhelp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('1,Setup test case')
    @classmethod
    def tearDownClass(cls):
        print('2,Tear down test case')

    def setUp(self):
        print('3,Set up test case')

    def tearDown(self):
        print('4,Tear down test case')

    def test_case01_getdefalutdisc(self):
        tel="13419591290"
        act_disc=MemberHelp.get_member_discount(tel)
        exp_disc=0.8
        self.assertEqual(exp_disc,act_disc)

    def test_case02_getdefalutdisc(self):
        tel="13312345678"
        act_disc=MemberHelp.get_member_discount(tel)
        exp_disc=1.0
        self.assertEqual(exp_disc,act_disc)

    def test_case03_getdefalutdisc(self):
        tel = "1349999999"
        act_disc = MemberHelp.get_member_discount(tel)
        exp_disc = "输入的手机号有误！"
        self.assertEqual(exp_disc,act_disc)

    def test_case04_getdefalutdisc(self):
        tel = "13499999999a"
        act_disc = MemberHelp.get_member_discount(tel)
        exp_disc = "输入的手机号好有误！"
        self.assertEqual(exp_disc,act_disc)




if __name__ == '__main__':
    unittest.main()
