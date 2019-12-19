import unittest
from Wangyunfei.shopping.test.test_homework.shopping import memberHelp

class MyTestCase(unittest.TestCase):
    def test_last(self):
        exp = memberHelp.select_member_last_four(1000)
        act = 'no'
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()
