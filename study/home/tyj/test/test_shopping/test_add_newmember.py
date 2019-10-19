import unittest
from tyj.homework0626.members import membershelp


class TestAddNewmember(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print ("1,Steup test class")
    @classmethod
    def tearDownClass(cls):
        print ("2,Tear Down test class")



    def test_case01(self):
        tel='18888888888'
        act_add=membershelp.add_new_member(tel)
        exp_add=1
        self.assertEqual(act_add, exp_add)

    def test_case02(self):
        tel='1'
        act_add=membershelp.add_new_member(tel)
        exp_add=1
        self.assertEqual(act_add, exp_add)

    def test_case03(self):
        tel='131'
        act_add=membershelp.add_new_member(tel)
        exp_add=False
        self.assertEqual(act_add, exp_add)

if __name__ == '__main__':
    unittest.main()
