#encoding:utf_8
members=[{'id':1,'tel':'18812345671','discount':0.95},
{'id':2,'tel':'18812345672','discount':0.9},
{'id':3,'tel':'18812345673','discount':0.85} ]


def get_member_discount( user_tel):
    for member in members:
        if member['tel'] == user_tel:
            print (member)
            return member['discount']

user_tel = raw_input('**********欢迎使用XXshopping系统************\n请输入你的手机号码:\n')
user_discount = get_member_discount(user_tel)
print (user_discount)