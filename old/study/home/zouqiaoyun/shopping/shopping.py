# coding:utf-8
from members import membersHelper
from client import Salesclient
# 定义一种获取会员信息的方法
def saling():

    u_tel=raw_input("请输入用户的手机号：")
    u_discount=membersHelper.get_member_discount(u_tel)
    # # 获取用户对商品信息的输入
    product_list=[]
    while True:
         product_info=Salesclient.get_product_input()
         if product_info=="Q":
            break
         else:
             str(product_info)
             product_list.append(product_info)

     # 依据输入的商品列表，计算商品的结算清单及总价

    pay_list,total=Salesclient.calcultor_payment(product_list,u_discount)


     # 格式化输出内容
    output=Salesclient.format_out_msg(pay_list,total)
    print(output)

if __name__=="__main__":
   saling()






