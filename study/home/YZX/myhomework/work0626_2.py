# encoding:utf-8
mermber = [
    {'id':1,'tel':'18845871680','zhekou':0.8},
    {'id':2,'tel':'18845095099','zhekou':0.88},
    {'id':1,'tel':'15165206762','zhekou':0.98}
]
wupin=[{'编号':'编号','价格':'价格','折后价格':'折后价格'}]
zhekou=1
tel=str(input('请输入你的手机号码：'))
count=0
for mem in mermber:
    count+=1
    if mem['tel']==tel:
        zhekou=mem['zhekou']
        print ("尊敬的会员，您的会员卡折扣为%f"%mem['zhekou'])
        break
    if count==len(mermber):
            print ("由于您不是会员，所以无法享受优惠")
while True:
    name = str(raw_input('请输入您购买的物品：'))
    if name == 'Q':
        break
    price = float(input('请输入您购买物品的原价：'))
    wupin.append({'id':len(wupin),'原价':price,'折后价':(price*zhekou)})
print (wupin[0]['编号']),
print (wupin[0]['价格']),
print (wupin[0]['折后价格'])
for i in range(1,len(wupin)):
    for wu in wupin:
        print wu
# for wu in wupin:
#     for wuu in wu:
#         print wuu['id']
print ("总价（SUM）：") ,
SP=0
for pri in wupin:
    SP+=pri['折后价']
    print (SP)
























