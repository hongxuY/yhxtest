# coding:utf-8
while True:
    try:
        i=float(raw_input("请输入当月利润（万）"))
        break
    except:
        print("请输入数字")
sum=0
if i>0 and i<=10:
    sum+=i*0.1
elif i>10 and i<=20:
    sum+=10*0.1+(i-10)*0.075
elif i>20 and i<=40:
    sum+=10*0.1+10*0.075+(i-20)*0.05
elif i>40 and i<=60:
    sum+=10*0.1+10*0.075+20*0.05+(i-40)*0.03
elif i>60 and i<=100:
    sum+=10*0.1+10*0.075+20*0.05+20*0.03+(i-60)*0.015
elif i>100:
    sum+=10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(i-100)*0.01
else:
    print("输入利润错误")
print("发放奖金总数：%f"%sum)
