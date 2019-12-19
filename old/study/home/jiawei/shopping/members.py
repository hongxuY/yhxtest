# encoding:utf-8
# 定义会员信息
members=[
    {'uid':'1','tel':'13419591290','disc':0.8}
]
class MemberHelp():
    # 定义一个获取会员信息的方法
    @classmethod
    def get_member_discount(cls,user_tel):
        for member in members:
            if member['tel']==user_tel:
                return member['disc']
        return 1.0



