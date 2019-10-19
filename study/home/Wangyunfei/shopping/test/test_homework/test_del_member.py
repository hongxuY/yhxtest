import unittest
from Wangyunfei.shopping.test.test_homework.shopping import memberHelp

class MyTestCase(unittest.TestCase):
    def test_del01(self):
        exp='no'
        act=memberHelp.del_member('18812345673')
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()
