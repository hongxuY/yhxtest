# encoding:utf-8
while True:
    try:
        a=input("请输入利润(单位万元):")
        break
    except:
        print ("请输入正确的数字")


if float(a)>10:
    if float(a)>10 and float(a)<=20:
        print ("奖金数额为:%f (单位万元)") %(10*0.1+(a-10)*0.075)
    elif float(a)>20 and float(a)<=40:
        print ("奖金数额为:%f (单位万元)") %(10*0.1+(20-10)*0.075+(a-20)*0.05)
    elif float(a)>40 and float(a)<=60:
        print ("奖金数额为:%f (单位万元)") % (10 * 0.1 + (20 - 10) * 0.075 + (40 - 20) * 0.05 + (a-40)*0.03)
    elif float(a)>60 and float(a)<=100:
        print ("奖金数额为:%f (单位万元)") % (10 * 0.1 + (20 - 10) * 0.075 + (40 - 20) * 0.05 + (60 - 40) * 0.03+(a-60)*0.015)
    elif float(a)>100:
        print ("奖金数额为:%f (单位万元)") % (
                    10 * 0.1 + (20 - 10) * 0.075 + (40 - 20) * 0.05 + (60 - 40) * 0.03 + (100 - 60) * 0.015 + (a-100)*0.01)
elif float(a)<=10 and float(a)>=0:
        print ("奖金数额为:%f (单位万元)") % (a * 0.1)
else:
    print ("继续努力吧,你没有奖金")