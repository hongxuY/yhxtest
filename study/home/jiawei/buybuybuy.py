#encoding:utf-8
members=[
    {'uid':'001','tel':'13419591290','disc':'0.8'}
]
# TODO 定义一个获取会员信息的方法
def get_member_discount(tel):
    # 如果是会员手机号，返回disc
    #如果不是会员手机号，返回1
    disc=0.95
    return disc
# TODO 获取用户的商品信息
demo_counter=0
def get_product_input():
    prod_info=raw_input('请输入商品的价格或者按Q进行结算:')
    global demo_counter
    demo_counter+=1
    if demo_counter ==2:
        return 'Q'
    return 100

# TODO 依据输入的商品列表，计算商品的结算清单及总价
def calculator_payment(prod_list):
#     待完善如何通过商品列表生成结算清单，并计算总价
    payment_list=[
        [1,100,90],
        [2,80,72]
    ]
    payment_total=162
    return payment_list,payment_total
# TODO 格式化输出内容
def format_out_msg(list,total):
#     待完善格式化
    out_msg="商品ID\t原价\t折后价\n"
    for prod in list:
        out_msg+="%s\t%s\t%s\n"%(prod[0],prod[1],prod[2])
    out_msg+='----------------------\n'
    out_msg+="总价：\t%s"%total
    return out_msg


    return out_msg


# 1.获取用户的手机号，并通过手机号码获取用户的折扣额度
# 获取客户的手机号码
user_tel=raw_input('请提供手机号码：')
# 通过提供的手机号码，获得他可以获得的折扣值
user_disc=get_member_discount(user_tel)

# 2.录入商品的信息
product_list=[]
while True:
    prod_info=get_product_input()
    if prod_info=='Q':
        break
    else:
        product_list.append(prod_info)

# 3.计算上平的结算清单
pay_list,pay_total=calculator_payment(product_list)

# 4.格式化输出内容
output=format_out_msg(pay_list,pay_total)

# 5.输出
print(output)