# encoding:utf-8
from members import MemberHelp
from client import Salesclient
def saling():
# 1.获取用户的手机号，并通过手机号码获取用户的折扣额度
# 获取客户的手机号码
    user_tel=raw_input('请提供手机号码：')
# 通过提供的手机号码，获得他可以获得的折扣值
    user_disc=MemberHelp.get_member_discount(user_tel)
# 2.录入商品的信息
    product_list=[]
    while True:
        prod_info=Salesclient.get_product_input()
        if prod_info=='Q':
            break
        else:
            product_list.append(prod_info)
# 3.计算上平的结算清单
    pay_list,pay_total=Salesclient.calculator_payment(product_list,user_disc)
# 4.格式化输出内容
    output=Salesclient.format_out_msg(pay_list,pay_total)
# 5.输出
    print(output)
if __name__=='__main__':
    saling()