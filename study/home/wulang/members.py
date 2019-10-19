# encoding:utf-8
# 定义会员的信息

members = [
    {'id': '1', 'tel': '13112345678', 'disc':0.9},
    {'id': '2', 'tel': '13212345678', 'disc': 0.95},
    {'id': '3', 'tel': '13312345678', 'disc': 0.8},
    {'id': '4', 'tel': '13412345678', 'disc': 0.7},
    {'id': '5', 'tel': '13512345678', 'disc': 0.85},
    {'id': '6', 'tel': '13612345678', 'disc': 0.75},
    {'id': '7', 'tel': '13712345678', 'disc': 0.65},
]

class MemberHelper():
    @classmethod
    def get_member_discount(self,user_tel):
         for member in members:
            if member["tel"] == user_tel:
                return member["disc"]
            return 1.0

 #新增
    @classmethod
    def add_member_by_tel(cls,tel):
        # for mem in members:
        #     if mem['tel']==tel:
        #         print ("已注册，注册失败")
        #         return False
        id=len(members)
        member={'id':'8','tel':13812345678,'disc':0.9}
        members.append(member)
        print ('注册成功')
        return 1
# add=Members()
# add.add_member_by_tell('18845871680')
# add.add_member_by_tell('111')
#获取所有会员列表全部信息
    @classmethod
    def get_members_all(cls):
        for mem in members:
            print ("会员编号：%s\t电话%s\t折扣%s\t"%(mem['id'],mem['tel'],mem['disc']))
        return 1
# all=Members()
# all.get_members_all()
#根据手机号的后四位获取会员信息
#根据手机号注销会员
#修改会员信息（手机号，折扣）
#会员可累积购物积分

# add=Members()
# add.add_member_by_tell('18845871680')
# add.add_member_by_tell('111')
#获取所有会员列表全部信息
# all=Members()
# all.get_members_all()
#根据手机号的后四位获取会员信息
    @classmethod
    def get_mermber_by_tell_last_four(cls,tel_last_four):
        for mem in members:
            i=float(mem['tel'])
            a=i%10000
            if tel_last_four==a:
                print ("会员编号：%s\t电话%s\t折扣%s\t"%(mem['id'],mem['tel'],mem['disc'],))
                return 1
        return False
# last_four=Members()
# last_four.get_mermber_by_tell_last_four(5099)
#根据手机号注销会员
    @classmethod
    def del_member_by_tell(cls,tel):
        for mem in members:
            if str(tel)==mem['tel']:
                mem['state']=0
                print ("删除成功")
                return 1
        print ("不存在该用户")
        return False
# del_by_tel=Members()
# del_by_tel.del_member_by_tell(18845871680)
#修改会员信息（手机号，折扣）
    @classmethod
    def modify_member_by_tel(cls,tel,disc):
        for mem in members:
            if str(tel)==mem['tel']:
                mem['disc']=disc
                print mem
                return 1
        print ("该手机未注册")
        return False
# member_modify=Members()
# member_modify.modify_member_by_tel(18845871680,0.2)
# member_modify.modify_member_by_tel(1884587168,0.2)
#会员可累积购物积分
    @classmethod
    def accumulated_shopping_points(cls,tel,sum):
        for mem in members:
            if str(tel)==mem['tel']:
                print ("找到会员，开始累计积分。")
                mem['points']+=sum
                if mem['points']<1000:
                    mem['disc']=1
                elif mem['points']>=1000 and mem['points']<3000:
                    mem['disc']=0.98
                elif mem['points']>=3000 and mem['points']<5000:
                    mem['disc'] = 0.98
                else:
                    mem['disc'] = 0.90
                print mem['disc']
                return mem['disc']
        print ("未找到该手机注册的会员，无法累计积分")
        return False
# accumulated=Members()
# accumulated.accumulated_shopping_points(18845871680,10000)
# accumulated.accumulated_shopping_points(111,1000)




