#encoding:utf-8

from zouqiaoyun.shopping1.members import  membersHelper1
from zouqiaoyun.shopping.client import  Salesclient

def saling():


#新增会员
    tel=raw_input("请输入新的电话号码：")
    membersHelper1.add_newmember(tel)

#获取会员列表信息
    membersHelper1.get_allmembers()

#根据手机号后四位获取会员信息
    lastfourtelnumber = raw_input("请输入手机号的后四位:")
    membersHelper1.get_member_list_by_lastfournumber(lastfourtelnumber)

#根据手机号注销会员
    tel=raw_input("请输入手机号码：")
    membersHelper1.zhuxiao_member(tel)

#修改会员信息（手机号和折扣）
    tel=raw_input("请输入用户手机号:")
    status=raw_input("请输入用户的状态：")
    print("选择如下如下:\n1：修改电话号码\n2：修改折扣\n3:电话号码和折扣都修改\n")
    update_choice=raw_input("请输入你的选择：")
    new_tel = raw_input("请输入新修改的号码:")
    new_discount = float(raw_input("请输入新修改的折扣:"))
    update_member=membersHelper1.update_member(tel,status,update_choice,new_tel,new_discount)

#获取折扣
    tel=raw_input("请输入用户的手机号：")
    u_disc=membersHelper1.get_member_discount(tel)
    print("你的折扣是：%s" %u_disc)


#获取用户对商品信息的输入
    product_list=[]
    while True:
         product_info=Salesclient.get_product_input()
         if product_info=="Q":
            break
         else:
             str(product_info)
             product_list.append(product_info)

#依据输入的商品列表，计算商品的结算清单及总价

    pay_list,total=Salesclient.calcultor_payment(product_list,u_disc)


#格式化输出内容
    output=Salesclient.format_out_msg(pay_list,total)
    print(output)


#会员可积累购物积分（1元=1积分，1000积分可以打98折，3000积分打95折，5000积分打九折）

    jifen=membersHelper1.accumulated_shopping_points(tel,total)













if __name__=="__main__":
    saling()