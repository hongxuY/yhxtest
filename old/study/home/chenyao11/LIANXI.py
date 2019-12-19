#encoding:utf-8
menbers=[
    {'id':'1','tel':'13312345671','discount':0.98},
    {'id':'2','tel':'13312345672','discount':0.9},
    {'id':'3','tel':'13312345673','discount':0.8}
]
tel=raw_input('请输入你的手机号：')
def get_menber_discount(tel):
    for member in menbers:
        if member['tel']==tel:
            return member['discount']
    return 1.0
disc=get_menber_discount(tel)

pro_list=[]
def get_pro_input():
    while True:
        try:
            shang=raw_input('请输入商品价格：')
            return float(shang)
        except:
            if shang=='Q':
               return 'Q'
            print('输入有误，请重新输入')
while True:
    pro_into=get_pro_input()
    if pro_into=='Q':
        break
    else:
        pro_list.append(pro_into)

def calculator_payment(pro_list,disc):
    pay_list=[]
    total=0
    for i in range(len(pro_list)):
        pay_item=[i+1,pro_list[i],pro_list[i]*disc]
        pay_list.append(pay_item)
        total+=pro_list[i]*disc
    return pay_list, total
payment_list,pay_total=calculator_payment(pro_list,disc)

def format_out_msg(list,total):
    out_msg='商品编号\t原价\t折后价\n'
    for pro in list:
        out_msg+='\t%s\t%s\t%s\n'%(pro[0],pro[1],pro[2])
    out_msg+='--------------\n'
    out_msg+='总价：%s'%total
    return out_msg
output=format_out_msg(payment_list,pay_total)

print(output)




