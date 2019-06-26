#coding:utf-8
while True:
    try:
        year = int(input("请输入年份：\n"))
        break
    except:
        print ("不正确输入")

if year==0:
    print ("没有公元0年")
elif year%400==0:
    print("%年是世纪闰年"%(year))
elif year%4==0 and year%100!=0:
    print("%d年是普通闰年"%(year))
else:
    print("%d年是平年"%(year))