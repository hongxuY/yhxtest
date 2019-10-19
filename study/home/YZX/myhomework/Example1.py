#encoding:utf-8
while 1:
    num=input("请输入月利润多少万元：")
    if float(num)<=10:
        print ("奖金为：%f万元"%(float(num)*0.10))
    elif float(num)>10 and float(num)<20:
        print ("奖金为：%f万元" % (1+(float(num)-10)*0.075))
    elif float(num)>=20 and float(num)<40:
        print ("奖金为：%f万元" % (1.75+(float(num)-20)*0.05))
    elif float(num)>=40 and float(num)<60:
        print ("奖金为：%f万元" % (2.75+(float(num)-40)*0.03))
    elif float(num)>=60 and float(num)<100:
        print ("奖金为：%f万元" % (3.35+(float(num)-60)*0.015))
    else:
        print ("奖金为：%f万元" % (3.95+(float(num)-100)*0.01))