#encoding:utf-8
#定义用户
mermber = [
    {'uid':1,'tel':'18845871680','disc':0.8},
    {'uid':2,'tel':'18845095099','disc':0.88},
    {'uid':1,'tel':'15165206762','disc':0.98}
]
#购买的商品,价格，折后价
goods_list=[['id','原价','折后价']]
#获得用户手机号码
def get_tel():
    tel=raw_input("请输入手机号码：")
    return  tel
# 获取会员折扣信息
# （判断是否为会员，非会员折扣为1，再根据会员的tel获取会员的折扣）
def get_disc_by_tel(tel):
    for me in mermber:
        if tel==me['tel']:
            return  me['disc']
    return 1.0
#输入商品
def get_goods_price():
    while True:
        try:
            good_price = raw_input("请输入购买商品的价格：")
            return float(good_price)
        except ValueError:
            if  good_price == 'Q':
                return 'Q'
            print("重新输入,请输入正确的商品价格")
# def get_goods():
#     while True:
#         try:
#             good_price = raw_input("请输入购买商品的价格：")
#             return float(good_price)
#         except ValueError:
#             if  good_price == 'Q':
#                 return 'Q'
#             print("重新输入,请输入正确的商品价格")
#         global disc
        # goods_list.append([len(goods_list),good_price],good_price*disc)
    # goods_list=[
    #     [1, 100, 90],
    #     [2, 200, 180]
    # ]
    # return goods_list
# 录入购买的商品,价格，折后价
def get_goods_list(get_price):
    global goods_list
    global disc
    if get_price=='Q':
        return
    goods_list.append([len(goods_list),get_price,float(get_price)*disc])
    return goods_list
#TODO 获得商品清单
#根据用户的购买列表来获得用户的购物清单，合计
# def get_shopping_list(goods_list):
#     shop_list=[
#         ['id','原价','折后价'],
#         goods_list
#     ]
#     return shop_list
#TODO 总计价格
def get_shopping_sum(shop_list):
    sum=0.0
    for su in shop_list:
        sum=float(su['折后价'])+sum
    return sum
# TODO 打印列表的方法
def output_shop_list(goods_list):
    for i in goods_list:
        count = 0
        for j in range(0, len(goods_list)):
            count += 1
            print i[j],
            if count == len(goods_list):
                print

#-----------------基本流程-----------------
#1.获得用户手机号码：
tel=get_tel()
#2.根据手机号码来获得本次购物的折扣：
disc=get_disc_by_tel(tel)
print (disc)
#3.获得录入用户购买的商品
while True:
    get_price=get_goods_price()
    if get_price=="Q":
        break
    else:
        # def get_goods_list(get_price):
        #     if get_price == 'Q':
        #         return
        #   goods_list.append([len(goods_list), get_price, get_price * disc])
        #   return goods_list
        get_goods_list(get_price)

#3.录入购买的商品,价格，折后价：
# shop_list=get_shopping_list(goods_list)
#4打印商品清单
# for i in output_shop_list:
#     count=0
#     for j in range(0,len(output_shop_list)):
#         count+=1
#         print i[j],
#         if count==len(output_shop_list):
#             print
output_shop_list(goods_list)
# print ("总计价格：%s"%get_shopping_sum(shop_list))