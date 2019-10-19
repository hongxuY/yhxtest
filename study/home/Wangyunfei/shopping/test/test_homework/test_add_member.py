import unittest
from Wangyunfei.shopping.test.test_homework.shopping import memberHelp


class TestmemberHelp(unittest.TestCase):
    def test_add_mem01(self):
        print('test_add_mem01')
        tel = '18812345665'
        act_disc = memberHelp.add_member_by_tel(tel)
        exp_disc = 1
        self.assertEqual(exp_disc, act_disc)
    def test_add_mem02(self):
        print('test_add_mem02')
        tel = '18812345671'
        act_disc = memberHelp.add_member_by_tel(tel)
        exp_disc = False
        self.assertEqual(exp_disc, act_disc)


if __name__ == '__main__':
    unittest.main()
