import unittest
from Wangyunfei.shopping.test.test_homework.shopping import memberHelp

class MyTestCase(unittest.TestCase):
    def test_jifen01(self):
        exp = False
        act = memberHelp.Cumulative_members_jifen(123,144)
        self.assertEqual(act, exp)

    def test_jifen02(self):
        exp =0.8
        act = memberHelp.Cumulative_members_jifen(18812345672,1500)
        self.assertEqual(act, exp)


if __name__ == '__main__':
    unittest.main()
