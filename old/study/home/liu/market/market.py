# encoding=utf-8
# members=[{'id':'1','tel':'188','disc':'0.9'},
# {'id':'2','tel':'188','disc':'0.8'},
# {'id':'3','tel':'188','disc':'0.7'}]
# #Todo 定义一个获取会员信息的函数
# #待完善
# def get_member_disc(u_tel):
#     for member in members:
#         if member['tel']==u_tel:
#             return member['disc']
#     return 1.0
#
# #Todo 获取用户对商品信息的输入
# prod_count=0
# def get_prod_input():
#     prod_info=raw_input('请输入商品价格或者Q进行结算：')

# #Todo 定义一个货物计价表
# #待完善
# def calculator_payment(prod):
#     payment_list=[
#         [1,100,90],
#         [2,90,81]
#     ]
#     payment_total=171
#     return payment_list,payment_total
# #
# #Todo 格式化输出内容
# #待完善
# def format_out_msg(list,total):
#     out_msg='''商品id\t原价\t折后价
#     1\t100\t90
#     2\t90\t81
#     -----------------
#     总价：\t171'''
#     return out_msg

#
#
#
#
#
# #1.获取用户手机号，并且获取相应折扣
#异常捕捉待完善
members=[{'id':'1','tel':'188','disc':0.9},
{'id':'2','tel':'187','disc':0.8},
{'id':'3','tel':'186','disc':0.7}]

def vip_tel():
 while True:
    try:
        u_tel=raw_input('请输入手机号码：')
        return u_tel
    except:
        print('输入有误，重新输入')
while True:
    u_tel=vip_tel()
    if len(u_tel)==3:
        break
    else:
        print('输入有误，重新输入')
def get_member_disc(u_tel):
    for member in members:
        if member['tel']==u_tel:
            return member['disc']
        return 1
u_disc=get_member_disc(u_tel)
def get_prod_input():
    while True:
        try:
            user_input=raw_input('请输入商品的价格或者Q进行结算：')
            return float(user_input)
        except ValueError:
            if user_input=="Q":
                return"Q"
        print('输入有误，重新输入')
prod_list=[]
while True:
    prod_info=get_prod_input()
    print('[DEBUG]:%s'%prod_info)
    if prod_info=="Q":
        break
    else:
        prod_list.append(prod_info)

# #3.计算商品账单
def calculator_payment(prod_list,u_disc):
    pay_list=[]
    total=0
    for i in range(len(prod_list)):
        pay_item=[i,prod_list[i],prod_list[i]*u_disc]
        pay_list.append(pay_item)
        total+=prod_list[i]*u_disc
    return pay_list,total
pay_list,total=calculator_payment(prod_list,u_disc)
print(pay_list)
print(total)
# #4.格式化输出内容
def format_out_msg(pay_list,total):
    out_msg='商品ID\t原价\t折后价\n'
    for prod in pay_list:
        out_msg+="%s\t%s\t%s\n"%(prod[0],prod[1],prod[2])
    out_msg += "------------------\n"
    out_msg +="总价:\t%s'"%total
    return out_msg
output=format_out_msg(pay_list,total)
print(output)



