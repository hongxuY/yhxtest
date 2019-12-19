#encoding:utf-8
mermber = [
    {'uid':1,'tel':'18845871680','disc':0.8},
    {'uid':2,'tel':'18845095099','disc':0.88},
    {'uid':1,'tel':'15165206762','disc':0.98}
]
goods_list=[]
def get_tel():
    tel=raw_input("请输入手机号码：")
    return  tel
def get_disc_by_tel(tel):
    for me in mermber:
        if tel==me['tel']:
            return  me['disc']
    return 1.0
def get_goods_price():
    while True:
        try:
            good_price = raw_input("请输入购买商品的价格：")
            return float(good_price)
        except ValueError:
            if  good_price == 'Q':
                return 'Q'
            print("重新输入,请输入正确的商品价格")
def get_shop_list(get_price,disc):
    pay_list=[]
    pay_sum=0
    for i in range(len(goods_list)):
        pay_item=[i+1,goods_list[i],goods_list[i]*disc]
        pay_list.append(pay_item)
        pay_sum+=goods_list[i]*disc
    return pay_list,pay_sum
def get_shopping_sum(shop_list):
    sum=0.0
    for su in shop_list:
        sum=float(su['折后价'])+sum
    return sum
def out_pay_list(list,sum):
    out_msg="商品ID\t单价\t折后价\n"
    for i in list:
        out_msg+="%s\t%s\t%s\n"%(i[0],i[1],i[2])
    out_msg+="---------------------"
    out_msg+="总计：\t%s"%sum
    return out_msg

tel=get_tel()
disc=get_disc_by_tel(tel)
print (disc)
while True:
    get_price=get_goods_price()
    if get_price=="Q":
        break
    else:
        goods_list.append(get_price)
pay_list,pay_sum=get_shop_list(get_price,disc)
print (pay_list)
print (pay_sum)
out_msg=pay_list(pay_list,pay_sum)
print (out_msg)

