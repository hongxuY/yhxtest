# coding:utf-8
##
members=[
    {'uid':'1','tel':'13312345678','disc':0.90},
    {'uid':'1','tel':'13312345679','disc':0.80},
    {'uid':'1','tel':'13312345677','disc':0.70}
        ]

def  get_memeber_discount(user_tel):
    for member in members:
         if member['tel']==user_tel:
          return member['disc']
    return 1.0
def get_product_input():
    while True:
        try:
           user_input=raw_input("请输入商品的价格或者Q进行结算：")
           return float(user_input)
        except:
           if user_input=="Q":
              return "Q"
        print ("输入错误，请重新输入")
def calculator_payment(pord_list,user_disc):
    payment_list=[]
    total=0
    for i in range(len(product_list)):
        payment_item=[i+1,pord_list[i],pord_list[i]*useer_disc]
        payment_list.append(payment_item)
        total+=pord_list[i]*useer_disc
    return payment_list,total
def format_out_msg(list,total):
    out_msg="商品ID\t原价\t折后价\n"
    for pord in list:
        out_msg+="%s\t%s\t%s\n"%(pord[0],pord[1],pord[2])
    out_msg+="--------------\n"
    out_msg+="总价:\t%s"%total
    return out_msg
#--------------------------------------------
useer_tel=raw_input("请输入手机号：")
useer_disc=get_memeber_discount(useer_tel)
print (useer_disc)
product_list=[]
while True:
    pord_info=get_product_input()
    if pord_info=="Q":
        break
    else:
        product_list.append(pord_info)
pay_list,pay_total=calculator_payment(product_list,useer_disc)
output=format_out_msg(pay_list,pay_total)
print (output)
product_list=[]
while True:
    product_info=get_product_input()
    if product_info=="Q":
        break
    else:
        product_list.append(product_info)
pay_list,pay_total=calculator_payment(product_list)
output=format_out_msg(pay_list,pay_total)
print(output)