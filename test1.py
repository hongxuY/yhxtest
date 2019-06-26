#coding:utf-8

lirun=float (raw_input("请输入利润（单位：万）"))

if lirun<=10:
    jianjin=lirun*0.1
elif lirun<=20:
    jianjin=10*0.1+(lirun-10)*0.075
elif lirun<=40:
    jianjin = 10 * 0.1 + 10 * 0.075 + (lirun-20)*0.05
elif lirun<=60:
    jianjin = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (lirun-40)*0.03
elif lirun<=100:
    jianjin = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03+(lirun-60)*0.015
else:
    jianjin = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015+(lirun-100)*0.01

print ("这个月的奖金是%d"%(jianjin))