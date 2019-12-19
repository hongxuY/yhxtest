# encoding:utf-8
while True:
    try:
        a = input("请输入年份:")
        break
    except:
        print ("输入有误,请输入正确的年份")



if int(a)>0:
        if int(a)%4==0 and int(a)%100!=0:
            print ("这是一个闰年")
        elif int(a)%400==0 and int(a)%1000!=0:
            print ("这是一个世纪闰年")
        elif int(a)%400==0 and int(a)%1000==0:
            print ("这是一个千禧年")
        else:
            print ("这不是闰年")
else:
        print ("输入有误,请输入正确的年份")