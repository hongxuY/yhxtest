# encoding:utf-8
from liu.market.client import client
members=[{'id':'1','tel':'188','disc':0.9},
{'id':'2','tel':'187','disc':0.8},
{'id':'3','tel':'186','disc':0.7}]

#获取折扣
class MembersHelp():
    @classmethod
    def get_member_disc(cls,u_tel):
        for member in members:
            if member['tel'] == u_tel:
                return member['disc']
        return 1.0
#新增
    @classmethod
    def add_members_vip(cls,u_tel):
        for member in members:
            if member['tel']==u_tel:
                print('账号已注册')
                return False
        id = len(members)+1
        member={'id':id,"tel":u_tel,'disc':1}
        members.append(member)
        print("注册成功")
#获取所有会员列表
    @classmethod
    def get_member_list(cls,u_tel):
        for member in members:
            if len(member['tel']%10000)==4:
                print(member)

#根据手机号注销会员（会员）
    @classmethod
    def logout_member(cls,u_tel):
        member={'id':id,"tel":u_tel,'disc':1,'status':0}
        for member in members:
            if member['tel'] == u_tel:
                member['status']==0
                return 'Logout Success'
        return False

#修改会员信息
    @classmethod
    def update_member(cls,u_tel):
        for member in members:
            if member['tel']==u_tel:
                new_tel=input('请输入新手机号：%d')
                member['tel']==new_tel
                new_disc=('请输入新的会员折扣：%d')
                member['disc']==new_disc
                print('修改成功！')
        else:
            print('请先注册会员！')

#会员累积购物积分
    @classmethod
    def accumulate_vip(cls,u_tel):
        member = {'id': id, "tel": u_tel, 'disc': 1, 'status': 0,'acu':'acu'}
        for member in members:
            if member['tel']==u_tel:







