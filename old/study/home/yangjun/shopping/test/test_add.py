import unittest

from yangjun.shopping.rembers import MemberHelper
class MyTestCase(unittest.TestCase):
    def test_something(self):
        tel="111"
        ex=1.0
        act=MemberHelper.add_rembers(tel)
        self.assertEqual(ex, act)

    def test_something2(self):
        tel = "18812345671"
        ex = False
        act = MemberHelper.add_rembers(tel)
        self.assertEqual(ex, act)


if __name__ == '__main__':
    unittest.main()
