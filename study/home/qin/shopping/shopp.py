#   coding:utf-8
from huiyuanxinxi import MemberHelper

members = [{'id':'2','tel':"18812345672",'discount':0.9}]
user_tel = raw_input('请输入手机号:')
def get_members_discount(tel):
    for member in members:
        if member['tel'] == user_tel:
            return member['discount']
        return 1
user_disc = get_members_discount(user_tel)
print (user_disc)

def get_product_input():
    while True:
        try:
           user_input = raw_input("请输入商品价格或是Q进行结算")
           return float(user_input)
        except ValueError:
            if user_input == "Q":
                return "Q"
            print ("输入错误，请重新输入")

product_list = []
while True:
    prod_info = get_product_input()
    # print ("[DEBUG]:%s" % prod_info)
    if prod_info == "Q":
        break
    else:
        # print ("[DEBUG] 已添加商品列表")
        product_list.append(prod_info)
# print ("[DEBUG] %s" % product_list)

def calculator_payment(prod_list,user_disc):
    payment_list = []
    total = 0
    for i in range(len(prod_list)):
        payment_item = [i +1,prod_list[i],prod_list[i]*user_disc]
        payment_list.append(payment_item)
        total += prod_list[i] * user_disc
    return payment_list,total
pay_list,pay_total = calculator_payment(product_list,user_disc)
print (pay_list)
print (pay_total)

def format_out_mas(list,total):
    out_mas = "商品ID\t原价\t折后价\n"
    for prod in list:
        out_mas += "%s\t%s\t%s\n" % (prod[0],prod[1],prod[2])
    out_mas += "———————————\n"
    out_mas += "总价：\t%s" % total
    return  out_mas
output = format_out_mas(pay_list,pay_total)
print (output)
