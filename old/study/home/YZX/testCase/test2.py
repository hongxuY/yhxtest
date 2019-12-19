# encoding:utf-8
members=[
    {'id':'1','tel':'13312345671','disc':0.98},
    {'id':'2','tel':'13312345672','disc':0.95},
    {'id':'3','tel':'13312345673','disc':0.9},
    {'id':'4','tel':'13312345674','disc':0.8}
]
tel=raw_input('请输入手机号：')

def get_member_discount(tel):
    for member in members:
        if member['tel']==tel:
            return member['disc']
    return 1.0
disc=get_member_discount(tel)

pro_list = []
def get_pro_input():
    while True:
        try:
            shang=raw_input('请输入商品价格或Q进行结算:')
            return float(shang)
        except:
            if shang =='Q':
                return 'Q'
            print('输入有误，请重新输入')
while True:
    pro_info=get_pro_input()
    if pro_info=='Q':
        break
    else:
        pro_list.append(pro_info)

def calculator_payment(pro_list,disc):
    payment_list=[]
    total=0
    for i in range(len(pro_list)):
        payment_item=[i+1,pro_list[i],pro_list[i]*disc]
        payment_list.append(payment_item)
        total+=pro_list[i]*disc
    return payment_list,total
pay_list,pay_total=calculator_payment(pro_list,disc)

def format_out_msg(list,total):
    out_msg='商品编号\t原价\t折后价\n'
    for pro in list:
        out_msg+='%s\t%s\t%s\n'%(pro[0],pro[1],pro[2])
    out_msg+='-------------\n'
    out_msg+='总价：\t%s'%total
    return out_msg
output=format_out_msg(pay_list,pay_total)
print(output)
