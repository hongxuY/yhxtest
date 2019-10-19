#encoding:utf-8
members=[
    {'uid':1,'tel':'13312345678','disc':0.9,'state':"live",'itg':5080},
    {'uid':2,'tel':'13312345679','disc':0.85,'state':"live",'itg':10880},
    {'uid':3,'tel':'13312345670','disc':0.95,'state':"live",'itg':3500},
    {'uid':4,'tel':'13419591290' ,'disc':0.98,'state':"die",'itg':1300}
]

class MemberAdmin():


# 添加会员
    @classmethod
    def MembersAdd(cls):
        # members = []
        while True:
            mem_info = raw_input('添加会员：\n输入T退出会员输入，输入Q录入会员信息！\n')
            if mem_info == "T":
                print("退出成功！")
                break
            elif mem_info == "Q":
                members_len = len(members)
                new_mem_tel = raw_input('请输入新增会员电话：')
                new_mem_disc = raw_input('请输入会员折扣信息：')
                new_mem_stat="live"
                new_mem_itg=0
                members.append({"uid": members_len + 1, 'tel': new_mem_tel, 'disc': new_mem_disc,'state':new_mem_stat,'itg':new_mem_itg})
                print ("添加会员成功！\n会员编号：%s\n会员电话：%s\n享受折扣：%s\n会员状态：%s\n会员积分：%s\n" %
                       (members_len + 1, new_mem_tel, new_mem_disc,new_mem_stat,new_mem_itg))


#  格式化输出会员信息
    @classmethod
    def vip_mem_import(cls):
        vip_msg = ("会员编号   会员电话       享受折扣 会员状态   会员积分\n")
        for member in members:
            vip_msg += "%s\t   %s\t     %s\t      %s\t       %s\n" % (member['uid'], member['tel'], member['disc'],member['state'],member['itg'])
        print vip_msg


# 根据手机号后四位，获得会员信息
    @classmethod
    def mem_tel_four(cls):
        mem_last_four = raw_input("请输入电话号码的后四位数：\n")
        n = list(mem_last_four)
        spp = []
        for member in members:
            tel = member["tel"]
            m = list(tel)
            if m[7:11] == n:
                spp.append(member)
        sel_vip_four_msg = ("会员编号   会员电话        享受折扣     会员状态    会员积分\n")
        for member in spp:
            sel_vip_four_msg += "   %s\t   %s\t    %s\t   %s\t   %s\n" % \
                                (member['uid'], member['tel'], member['disc'],member['state'],member['itg'])
        print sel_vip_four_msg


# 注销会员
    @classmethod
    def member_cancel(cls):
        mem_tel_cancel=raw_input('请输入要注销的会员手机号：')
        for member in members:
            if mem_tel_cancel==member['tel']:
               member['state']='die'
               sel_vip_four_msg = ("会员编号   会员电话        享受折扣     会员状态    会员积分\n")
               sel_vip_four_msg += "   %s\t   %s\t    %s\t        %s\t    %s\n" %\
                                   (member['uid'], member['tel'], member['disc'], member['state'],member['itg'])
               print('注销成功！')
               print sel_vip_four_msg


# 修改会员信息
    @classmethod
    def change_members(cls):
        mem_tel_change=raw_input('请输入要更改的会员手机号:')
        for member in members:
                if mem_tel_change==member['tel'] and member['state']=='die':
                    print('此会员已经注销！')
                    input_new_num = raw_input('请输入新的手机号：\n')
                    input_new_disc = raw_input('请输入新的折扣信息：\n')
                    member['disc'] = input_new_disc
                    member['state'] = "live"
                    member['tel'] = input_new_num
                    print('修改成功！')
                    print member
                if mem_tel_change==member['tel'] and member['state']=='live':
                    print('此号码已经是会员！')
                    input_new_num = raw_input('请输入新的手机号：\n')
                    input_new_disc = raw_input('请输入新的折扣信息：\n')
                    member['disc'] = input_new_disc
                    member['state'] = "live"
                    member['tel'] = input_new_num
                    print('修改成功！')
                    print member
                # else :
                #     print('此号码不是会员！')

# 会员积分更改
    @classmethod
    def chg_mem_integrace(cls):
        xfje = int(raw_input('请输入本次消费的金额：\n'))
        mem_tel = raw_input('请输入会员电话号码:\n')
        for member in members:

            if member['tel']==mem_tel:
                member['itg']+=xfje
                if member['itg']>10000:
                    member['disc']='0.88'

                elif 5000<member['itg']<=10000:
                    member['disc']=0.9
                elif 3000<member['itg']<=5000:
                    member['disc']=0.95
                elif 1000<member['itg']<=3000:
                    member['disc']=0.98
                else:
                    member['disc']=1.0
                sel_vip_four_msg = ("会员编号   会员电话        享受折扣     会员状态    会员积分\n")
                sel_vip_four_msg += "   %s\t   %s\t    %s\t       %s\t         %s\n" % \
                                    (member['uid'], member['tel'], member['disc'], member['state'], member['itg'])
                print sel_vip_four_msg

