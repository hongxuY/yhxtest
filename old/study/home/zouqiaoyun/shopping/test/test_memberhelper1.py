# coding:utf-8
import unittest
from zouqiaoyun.shopping1.members import membersHelper1
from zouqiaoyun.shopping.client import  Salesclient


class TestmembersHelper1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up test case")

    @classmethod
    def tearDownClass(cls):
        print("tear down test case")

#测试增加会员
    def test_case01_addmember1(self):
        tel="13590177836"
        act_result=membersHelper1.add_newmember(tel)
        exc_result={'status': 'active', 'discount': 0.9, 'tel': '13590177836', 'id': 5, 'jifen': 0}
        self.assertEqual(exc_result, act_result)

    def test_case02_addmember1(self):
        tel="12590178902"
        act_result=membersHelper1.add_newmember(tel)
        exc_result={'status': 'active', 'discount': 0.9, 'tel': '12590178902', 'id': 5, 'jifen': 0}
        self.assertEqual(exc_result, act_result)

    def test_case03_addmember1(self):
        tel="13350332123"
        act_result=membersHelper1.add_newmember(tel)
        exc_result={'status': 'active', 'discount': 0.9, 'tel': '13350332123', 'id': 5, 'jifen': 0}
        self.assertEqual(exc_result, act_result)

# 获取会员列表
    def test_case01_get_members_list(self):
        input=""
        act_result=membersHelper1.get_allmembers()
        exc_result=1.0
        self.assertEqual(exc_result, act_result)

    def test_case02_get_members_list(self):
        input="13112345678"
        act_result=membersHelper1.get_allmembers()
        exc_result=1.0
        self.assertEqual(exc_result, act_result)

    def test_case03_get_members_list(self):
        input="asdfghjkl"
        act_result=membersHelper1.get_allmembers()
        exc_result=1.0
        self.assertEqual(exc_result, act_result)

#根据手机后四位获取会员信息
    def test_case01_lastfourname(self):
        lastfourtelnumber="1234"
        act_result=membersHelper1.get_member_list_by_lastfournumber(lastfourtelnumber)
        exc_result=[{'status': 'active', 'discount': 0.8, 'tel': '18902371234', 'id': '1', 'jifen': 0}]
        self.assertEqual(exc_result, act_result)

    def test_case02_lastfourname(self):
        lastfourtelnumber="aaa"
        act_result=membersHelper1.get_member_list_by_lastfournumber(lastfourtelnumber)
        exc_result=[{'status': 'active', 'discount': 0.8, 'tel': '1890237aaaa', 'id': '1', 'jifen': 0}]
        self.assertEqual(exc_result, act_result)

    def test_case03_lastfourname(self):
        lastfourtelnumber="？"
        act_result=membersHelper1.get_member_list_by_lastfournumber(lastfourtelnumber)
        exc_result=[{'status': 'active', 'discount': 0.8, 'tel': '1890237？', 'id': '1', 'jifen': 0}]
        self.assertEqual(exc_result, act_result)


#注销会员
    def test_case01_zhuxiao(self):
        tel="12590178902"
        act_result=membersHelper1.zhuxiao_member(tel)
        exc_result={'status': 'inactive', 'discount': 0.98, 'tel': '12590178902', 'id': '4', 'jifen': 0}
        self.assertEqual(exc_result, act_result)

    def test_case02_zhuxiao(self):
        tel="1350aaaaaaa"
        act_result=membersHelper1.zhuxiao_member(tel)
        exc_result={'status': 'inactive', 'discount': 0.98, 'tel': '1350aaaaaaa', 'id': '4', 'jifen': 0}
        self.assertEqual(exc_result, act_result)

    def test_case03_zhuxiao(self):
        tel="#"
        act_result=membersHelper1.zhuxiao_member(tel)
        exc_result={'status': 'inactive', 'discount': 0.98, 'tel': '#', 'id': '4', 'jifen': 0}
        self.assertEqual(exc_result, act_result)

#修改会员信息
    def test_case01_update(self):
        tel="18902371234"
        status="active"
        newtel="18902371235"
        choose="1"
        newdiscount="0.9"
        act_result=membersHelper1.update_member(tel,status,choose,newtel,newdiscount)
        exc_result={'discount': 0.8,'id': 1, 'jifen': 0, 'status': 'active', 'tel': '18902371235'}
        self.assertEqual(exc_result, act_result)

    def test_case02_update(self):
        tel="#"
        status="active"
        newtel="18902371235"
        choose="1"
        newdiscount="0.9"
        act_result=membersHelper1.update_member(tel,status,choose,newtel,newdiscount)
        exc_result={'status': 'active', 'discount': 0.8, 'tel': '18902371235', 'id': 1, 'jifen': 0}
        self.assertEqual(exc_result, act_result)



if __name__ == '__main__':
    unittest.main()
