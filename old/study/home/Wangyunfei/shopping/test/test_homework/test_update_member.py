import unittest
from Wangyunfei.shopping.test.test_homework.shopping import memberHelp


class TestmemberUpdate(unittest.TestCase):
    def test_update_mem01(self):
        print('test_update_mem01')
        exp='no'
        act=memberHelp.update_member(18812345673,0.6)
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()
