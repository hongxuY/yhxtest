#encoding:utf-8
mermber = [
    {'id':1,'tel':'18845871680','zhekou':0.8},
    {'id':2,'tel':'18845095099','zhekou':0.88},
    {'id':1,'tel':'15165206762','zhekou':0.98}
]
tel=str(input('请输入你的手机号码：'))
count=0
zhekou=1
for mem in mermber:
    count+=1
    if mem['tel']==tel:
        zhekou=mem['zhekou']
        print ("尊敬的会员，您的会员卡折扣为%f"%mem['zhekou'])
        break
    if count==len(mermber):
            print ("由于您不是会员，所以无法享受优惠")
wupin=['id','Original','Discount']
wupin1=[]
while True:
    name = raw_input('请输入您购买的物品：')
    if name == 'Q':
        break
    price = float(raw_input('请输入您购买物品的原价：'))
    wupin1.append({'id':len(wupin),'Original':price,'Discount':(price*zhekou)})
for wu in wupin:
       print wu   ,
