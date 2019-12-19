import unittest
from Wangyunfei.shopping.test.test_homework.shopping import memberHelp

class memberHelp(unittest.TestCase):
    def test_select_mem01(self):
        exp=1
        act=memberHelp.select_member()
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()
