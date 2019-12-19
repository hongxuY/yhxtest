# encoding:utf-8

from members import membershelp
from client import salesclient

def saling():
    # 1.获取用户手机号，并通过手机号判断是否会员，返回会员折扣
    user_tel = raw_input('请输入手机号')
    user_disc = membershelp.member_disc(user_tel)
    # 2.录入商品信息
    goods_list = []
    while True:
            prod_info = salesclient.get_product_input()
            print ('商品价格为：%s'% prod_info)
            if prod_info =="Q":
                break
            else:
                goods_list.append(prod_info)
    print ("商品清单 %s" %goods_list)
    # 3.计算商品的结算清单
    pay_list,pay_total=salesclient.payment(goods_list,user_disc)
    # 4.格式化输出内容
    out_put=salesclient.format_out_msg(pay_list, pay_total )
    print (out_put)
if __name__=='__main__':
    saling()


