import unittest
from zouqiaoyun.shopping.members import membersHelper

class TestmembersHelper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("1,set up test case")

    @classmethod
    def tearDownClass(cls):
        print("2,tear down test case")

    def setUp(self):
        print("3,set up test case")


    def tearDown(self):
        print("4,tear down test case")


    def test_case01_getddfaultdisc(self):
        print("5,case01")
        tel="18902371234"
        act_disc=membersHelper.get_member_discount(tel)
        exc_disc=0.8
        self.assertEqual(exc_disc, act_disc)

    def test_case02_get0p9disc(self):
        print("6,case02")
        tel="18302531230"
        act_disc=membersHelper.get_member_discount(tel)
        exc_disc=0.9
        self.assertEqual(exc_disc, act_disc)

    def test_case03_get0p95disc(self):
        print("7,case03")
        tel="13503321236"
        act_disc=membersHelper.get_member_discount(tel)
        exc_disc=0.95
        self.assertEqual(exc_disc, act_disc)

    def test_case04_nonedisc(self):
        print("8,case04")
        tel="#"
        act_disc=membersHelper.get_member_discount(tel)
        exc_disc=1.0
        self.assertEqual(exc_disc, act_disc)

if __name__ == '__main__':
    unittest.main()
