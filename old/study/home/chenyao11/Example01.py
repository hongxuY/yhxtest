# encoding:utf-8
a = float(raw_input('请输入当月利润：'))
if a<0:
    print("没有奖金")
elif a <= 10 and a>=0:
    print ('发放奖金总数为：%.4f万元'%(0.1*a))
elif a >10 and a<=20:
    print ('发放奖金总数为：%.4f万元' % (1+(a-10)*0.075))
elif a>20 and a<=40:
    print ('发放奖金总数为：%.4f万元' % (1.75+(a-20)*0.05))
elif a>40 and a <=60:
    print ('发放奖金总数为：%.4f万元' % (2.75+(a-40) * 0.03))
elif a>60 and a<=100:
    print ('发放奖金总数为：%.4f万元' % (3.35+(a-60)*0.015))
else:
    print ('发放奖金总数为：%.4f万元' % (3.95+(float(a)-100)*0.01))
