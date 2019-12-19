# encoding:utf-8
a=input('请输入利润值')
if float(a)>10:
    if float(a)>10 and float(a)<=20:
       b=(a-10)*0.075+10*0.1
       print('奖金发放总数为%f万'%b)
    elif float(a)>20 and float(a)<=40:
        b=10*0.1+10*0.075+(a-20)*0.05
        print('奖金发放总数为%f万' % b)
    elif float(a)>40 and float(a)<=60:
        b=10*0.1+10*0.075+20*0.05+(a-40)*0.03
        print('奖金发放总数为%f万' % b)
    elif float(a)> 60 and float(a)<=100:
        b=10*0.1+10*0.075+20*0.05+20*0.03+(a-60)*0.015
        print('奖金发放总数为%f万' % b)
    elif float(a)>100:
        b = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015+(a-100)*0.01
        print('奖金发放总数为%f万' % b)
elif float(a)>=0 and float(a)<=10:
    b=a*0.1
    print('奖金发放总数为%f万' % b)
else:
    print('对不起您没有奖金')
