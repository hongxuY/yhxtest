# coding:utf-8

# kandaoxigua = True
# meikandaoxigua=False
# if  meikandaoxigua:
#     print('''
#     看到西瓜了,
#     买五个包子，
#     买了一个西瓜''')
# else:
#     print ("买五个包子")

a=float(input("当月利润："))
m=float()
if 0<=a<=10:
    m=a*0.1
    print ("当月奖金：(万元)")
    print (m)
if 10<a<=20:
    m=(a-10)*0.075+1
    print ("当月奖金：(万元)")
    print (m)
if 20<a<=40:
    m=(a-20)*0.05+10*0.075+1
    print ("当月奖金：(万元)")
    print (m)
if 40<a<=60:
    m=(a-40)*0.03+20*0.05+10*0.075+1
    print ("当月奖金：(万元)")
    print (m)
if 60<a<=100:
    m=(a-60)*0.015+20*0.03+20*0.05+10*0.075+1
    print ("当月奖金：(万元)")
    print (m)
if a>100:
    m=(a-100)*0.01+40*0.015+20*0.03+20*0.05+10*0.075+1
    print ("当月奖金：(万元)")
    print (m)
else:
    print ("输入错误")





