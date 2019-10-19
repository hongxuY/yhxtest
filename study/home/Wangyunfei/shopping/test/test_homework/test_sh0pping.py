import unittest
from Wangyunfei.shopping.test.test_homework.shopping import  memberHelp


class TestmemberHelp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('1,set up test class\n')
    @classmethod
    def tearDownClass(cls):
        print('2,tear down test class\n')

    def setUp(self):
        print('3,set up test case\n')

    def tearDown(self):
        print('4,tear down test case\n')

    def test_case01(self):
        print('5,test_case01\n')
        tel='18812345671'
        act_disc=memberHelp.get_member_discount(tel)
        exp_disc=0.98
        self.assertEqual(exp_disc, act_disc)

    def test_case02(self):
        print('6,test_case02\n')
        tel='18817654321'
        act_disc=memberHelp.get_member_discount(tel)
        exp_disc=1.0
        self.assertEqual(exp_disc, act_disc)

    def test_case03(self):
        print('7,test_case03\n')
        tel='18817654aaa'
        act_disc=memberHelp.get_member_discount(tel)
        exp_disc=0.98
        self.assertEqual(exp_disc, act_disc)


if __name__ == '__main__':
    unittest.main()
