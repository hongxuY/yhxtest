import unittest

from tyj.homework0626.members import membershelp

class TestMemberHelper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print ("1,Steup test class")
    @classmethod
    def tearDownClass(cls):
        print ("2,Tear Down test class")
    # def setUp(self):
    #     print ('3,Set up test case')
    # def tearDown(self):
    #     print ('4,Tear down test case')

    def test_case01(self):
        tel = "131"
        act_disc = membershelp.member_disc(tel)
        exp_disc = 0.98
        self.assertEqual(exp_disc, act_disc)
    def test_case02(self):
        tel = "132"
        act_disc = membershelp.member_disc(tel)
        exp_disc = 0.9
        self.assertEqual(exp_disc, act_disc)
    def test_case03(self):
        tel = "135"
        act_disc = membershelp.member_disc(tel)
        exp_disc = 0.8
        self.assertEqual(exp_disc, act_disc)
if __name__ == '__main__':
    unittest.main()
