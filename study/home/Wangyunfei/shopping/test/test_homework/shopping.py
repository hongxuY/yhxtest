# coding:utf-8
members=[
    {'id':1,'tel':'18812345671','discount':0.98,'state':1,'jifen':1000},
    {'id':2,'tel':'18812345672','discount':0.9,'state':1,'jifen':1500},
    {'id':3,'tel':'18812345673','discount':0.8,'state':1,'jifen':2000}
]

class memberHelp():
    @classmethod
    def get_member_discount(cls,user_tel):
        for member in members:
            if member['tel'] == user_tel:
               return  member['discount']
        return 1.0


# 新增
    @classmethod
    def add_member_by_tel(cls,tel):
        for mem in members:
            if float(mem['tel'])==tel:
                print('该用户已存在')
                return False
            id=len(members)+1
            mem=[{id:'id','tel':tel,'discount':1}]
            members.append(mem)
            print('会员添加成功')
            print members
            return 1
# c=memberHelp()
# c.add_member_by_tel(1283)

# 获取所有会员列表
    @classmethod
    def select_member(cls):
        for mem in members:
            print('编号%s\t电话%s\t折扣%s\t状态%s\t积分\t'%(mem['id'],mem['tel'],mem['disc'],mem['state'],mem['jifen']))
        return



# 根据手机号的后4位获取会员信息

    @classmethod
    def select_member_last_four(cls,last_tel_four):
        for mem in members:
            a = float(members['tel']) % 10000
            if last_tel_four==a:
                print('编号%s\t电话%s\t折扣%s\t状态%s\t积分\t'%(mem['id'],mem['tel'],mem['disc'],mem['state'],mem['jifen']))
            return 1

# 根据手机号注销会员
    @classmethod
    def del_member(cls,tel):
        for mem in members:
            if str(tel)==members('tel'):
                mem['state']=0
                print('注销成功')
                return 'yes'
            print('注销失败，该手机号不是会员')
            return 'no'

# 修改会员信息(折扣，手机号）
    @classmethod
    def update_member(cls,tel):
        for mem in members:
            if str[tel]==members['tel']:
                mem['discount']=='discount'
                print mem
                return 'yes'
            print('该用户未注册')
            return 'no'

# 会员累计购物积分
    @classmethod
    def Cumulative_members_jifen(cls,tel,sum):
        for mem in members:
            if str(tel)==mem['tel'] and mem['state']==1:
                mem['jifen']+=sum
                if mem['jifen']<1000:
                    print(mem['jifen']==1)
                elif mem['jifen']>=1000 and mem['jifen']<1500:
                    print(mem['jifen'] == 0.98)
                elif mem['jifen'] >= 1500 and mem['jifen'] < 2000:
                    print(mem['jifen'] == 0.9)
                elif mem['jifen'] >= 2000 :
                    print(mem['jifen'] == 0.8)
                return mem['discount']
        print('对不起您不是会员，无法进行积分累计')
        return False
















