#coding:utf-8
try:
    year = int(input("请输入年份："))
except NameError:
    year="不正确输入"
except SyntaxError:
    year = "不正确输入"

if year=="不正确输入":
    print("输入有误，请输入正确的数字年份")
elif year==0:
    print ("没有公元0年")
elif year%400==0:
    print("%d是世纪闰年"%(year))
elif year%4==0 and year%100!=0:
    print("%d是普通闰年"%(year))
else:
    print("%d是平年"%(year))