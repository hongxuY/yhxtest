#   coding:utf-8

# 会员信息
members = [{'id':'2','tel':"18812345672",'discount':0.9},
           {'id':'3','tel':"18812345673",'discount':0.8}
        ]

class MemberHelper():


    @classmethod
    def get_members_discount(self,user_tel):
        for member in members:
            if member['tel'] == user_tel:
                return member['discount']
            return 1

user_disc = MemberHelper().get_members_discount("18812345672")
print (user_disc)
user_disc2 = MemberHelper().get_members_discount("1111")
print (user_disc2)

