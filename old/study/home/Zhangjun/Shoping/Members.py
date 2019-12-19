#encoding:utf_8
members=[{'id':1,'tel':'18812345671','discount':0.95,'sta':1},
{'id':2,'tel':'18812345672','discount':0.9,'sta':1},
{'id':3,'tel':'18812345673','discount':0.85,'sta':1} ]


class MembersHelp():

    @classmethod
    def get_member_discount(cls,user_tel):
        for member in members:
            if member['tel'] == user_tel:
               print ('尊敬的会员用户你好！')
               i = int(input('请输入你的选择：1.注销会员;2.修改会员;3.查看会员信息；4.查看所有会员（店主使用）5.跳过\n'))
               if i == 1:
                  member['sta'] = 2
                  print ('你的会员注销成功！你的会员信息是:%s' % member)
                  return 1.0
               elif i==2:
                   member['tel'] = raw_input('请输入你的新手机号')
                   member['discount'] = float(raw_input('请输入你想办的会员折扣'))
                   print ('你的会员修改成功！你的会员信息是:%s' % member)
                   return member['discount']
               elif i==3:
                    l_tel = float(raw_input('请输入手机后四位,查询你的会员信息'))
                    float(member['tel'])
                    i = float(member['tel']) % 10000
                    if i == l_tel:
                       print ('这是你的会员信息：%s' % member)
                    return member
               elif i==4:
                    print ('本店的会员信息为：%s'%members)
                    return members
               else:
                    return  member['discount']
        else:
            print ('你还不是本店的会员，你是否愿意办理会员？')
            i = int(input('请输入你的选择:1.是;2.否\n'))
            if i==1:
                new_id=len(members)+1
                new_discount=float(input('请输入你要办理的会员折扣:0.90;0.95;0.98\n'))
                dic={'id':new_id,'tel':user_tel,'discount':new_discount,'sta':1,'integral':0}
                members.append(dic)
                print ('你的会员办理成功！你的会员信息是:%s'%dic)
                return new_discount
            return 1.0

    #
    # # 查询会员信息
    # @classmethod
    # def sel_member(cls,l_tel):
    #     for member in members:
    #         float(member['tel'])
    #         i = float(member['tel']) % 10000
    #         if i==l_tel:
    #            print ('这是你的会员信息：%s' %member)





    # 会员可积累积分：
    # @classmethod
    # def get_member_jifen(cls,user_tel,integral):
    #     for member in members:
    #         if member['tel'] == user_tel:
    #             print (integral)
    #             if 1000<='integral'<3000:
    #                member['discount']=0.98
    #             if 3000 <= 'integral' < 5000:
    #                 member['discount']=0.95
    #             if 5000 <= 'integral' :
    #                 member['discount']=0.90


