#encoding:utf-8
from jiawei.shopping.vip_message.member_cancel import MemberAdmin

while True:
    sel_choice=raw_input("请选择你要进行的操作\n按1：添加会员\n按2：查询所有的会员\n"
                         "按3：获取会员信息\n按4：注销会员\n按5：修改会员信息\n按6：会员积分修改\n")
    if sel_choice=='1':
       vip_mem_adds=MemberAdmin.MembersAdd()

    elif sel_choice=='2':
        vip_mem_select=MemberAdmin.vip_mem_import()

    elif sel_choice=='3':
       vip_mem_information=MemberAdmin.mem_tel_four()

    elif sel_choice=='4':
        vip_mem_cancel=MemberAdmin.member_cancel()

    elif sel_choice=='5':
        vip_mem_change=MemberAdmin.change_members()

    elif sel_choice=='6':
        vip_mem_integral=MemberAdmin.chg_mem_integrace()

    else:
        print("选择错误，请重新选择！")

