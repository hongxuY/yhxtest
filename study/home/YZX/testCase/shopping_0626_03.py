#encoding:utf-8
#定义用户
mermber = [
    {'uid':1,'tel':'18845871680','disc':0.8},
    {'uid':2,'tel':'18845095099','disc':0.88},
    {'uid':1,'tel':'15165206762','disc':0.98}
]
#购买的商品,价格，折后价
goods_list=[]
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
#TODO 输入商品
def get_goods():
    while True:
        try:
            good_name = raw_input("请输入购买的商品：")
            if good_name == 'Q':
                break
            good_price = float(raw_input("请输入购买商品的价格："))
        except:
            print("请输入正确的商品和价格")
            continue
        goods_list.append([len(goods_list),good_name,good_price])
    # goods_list=[
    #     [1, 100, 90],
    #     [2, 200, 180]
    # ]
    return goods_list
#TODO 录入购买的商品,价格，折后价
def get_goods_list(get_goods):
    goods_list=[
        [1,100,90],
        [2,200,180]
    ]
    return goods_list
#TODO 获得商品清单
#根据用户的购买列表来获得用户的购物清单，合计
def get_shopping_list(goods_list):
    shop_list=[
        ['id','原价','折后价'],
        [1,100,90],
        [2,200,180]
    ]
    return shop_list
#TODO 总计价格
def get_shopping_sum(shop_list):
    shop_sum = ['总计：', 270]
    return shop_sum
# TODO 打印列表的方法

#-----------------基本流程-----------------
#1.获得用户手机号码：
tel=get_tel()
#2.根据手机号码来获得本次购物的折扣：
disc=get_disc_by_tel(tel)
print (disc)
#3.获得录入用户购买的商品
buy_goods=get_goods()
#3.录入购买的商品,价格，折后价：
goods_list=get_goods_list(buy_goods)
#4获得商品清单 总价格
output_shop_list=get_shopping_list(goods_list)
output_shop_sum=get_shopping_sum(output_shop_list)
#5打印商品清单
for i in output_shop_list:
    count=0
    for j in range(0,len(output_shop_list)):
        count+=1
        print i[j],
        if count==len(output_shop_list):
            print
print output_shop_sum[0],
print  output_shop_sum[1]
