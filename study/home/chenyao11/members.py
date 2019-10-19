# encoding:utf-8
members=[
    {'id':'1','tel':'13312345671','disc':0.98},
    {'id':'2','tel':'13312345672','disc':0.95},
    {'id':'3','tel':'13312345673','disc':0.9},
    {'id':'4','tel':'13312345674','disc':0.8}
]
# tel=raw_input('请输入手机号：')
#print(type(tel))
class MemberHelper(object):
    #定义一个可以获取会员信息的办法
    @classmethod
    def get_member_discount(cls,tel):
        for member in members:
            if member['tel']==tel:
                return member['disc']
        return 1.0
# disc=get_member_discount(tel)
user_disc=MemberHelper.get_member_discount('13312345674')
print(user_disc)
user_disc1=MemberHelper.get_member_discount('133')
print(user_disc1)




