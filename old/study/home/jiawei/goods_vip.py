#encoding:utf-8
# 定义会员的信息
members=[
    {"uid":0001,"tel":'159','discount':0.98},
    {"uid":0002,"tel":'15998765431','discount':0.9},
    {"uid":0003,"tel":'15998765430','discount':0.8}
]
# 定义了一个方法，来获取会员的信息
def get_member_discount(user_tel):
    for member in members:
        if member['tel']==user_tel:
            return member['discount']

    return 1.0
     # 如果是会员手机号，返回disc
    # 如果不是会员手机号，返回1


#  获取用户对商品信息的输入
def get_product_input():
    while True:
        try:
            user_input=raw_input('请输入商品的价格或是Q结束：\n')
            return float(user_input)
        except :
            if user_input =="Q":
                return'Q'
            print('输入错误，请重新输入')


#
#     else:
#         print('[DEBUG] 以添加商品列表')
# demo_counter=0
# # def get_product_input():
# #     # 待完善的异常捕获和处理
# #     prod_info=raw_input("请输入商品的价格或是Q进行结算：")
# #     global demo_counter
# #     demo_counter+=1
# #     if demo_counter ==2:
# #         return "Q"
# #
# #     return 100

#  依据输入的商品列表，计算商品的结算清单及总价
def calculator_payment(prod_list,user_disc):
    payment_list=[]
    total=0
    for i in range(len(prod_list)):
        payment_item=[i+1,prod_list[i],prod_list[i]*user_disc]
        payment_list.append(payment_item)
        total+=prod_list[i]*user_disc
    return payment_list,total


#  格式化输出结果

def format_out_msg(list,total):
    out_msg="商品ID\t原价\t折后价\n"
    for prod in list:
        out_msg+="%s\t%s\t%s\n"%(prod[0],prod[1],prod[2])
    out_msg+='-------------------\n'
    out_msg+="总价：\t%s"%total
    return out_msg
# 1.获取用户的手机号，并通过手机号码获取用户的折扣额度
user_tel=raw_input('请提供手机号码：')
user_dics=get_member_discount(user_tel)
print(user_dics)


# 2.录入商品信息
product_list=[]
# def get_product_input():
#
#     while True:
#         try:
#             user_input=raw_input('请输入商品的信息，按Q结算：\n')
#             return float(user_input)
#         except ValueError:
#             if user_input =='Q':
#                 return 'Q'
#             print('输入错误，请重新输入！')

while True:
    prod_info=get_product_input()
    print('[DEBUQ]:%s'%prod_info)
    if prod_info=="Q":
        break
    else:
        print('[DEBUG]已添加商品列表')
        product_list.append(prod_info)
print('[DEBUG]%s'%product_list)

# 3.计算商品的结算清单

# def calculator_payment(prod_list,user_disc):
#     payment_list=[]
#     total=0
#     for i in range(len(prod_list)):
#         payment_item=[i+1,prod_list[i],prod_list[i]*user_disc]
#         payment_list.append(payment_item)
#         total+=prod_list[i]*user_disc
#     return payment_list,total
pay_list,pay_total=calculator_payment(product_list,user_dics)

# 4.格式化输出内容

output=format_out_msg(pay_list,pay_total)

# 5.输出
print(output)
