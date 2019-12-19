#encoding:utf-8
while 1:
    year=input("请输入判断的年份：")
    if int(year) < 0:
        print ("年份不能为负")
        break
    if int(year)%100==0:
        if int(year)%400==0:
            print ("%d是闰年"%int(year))
        else:
            print ("%d不是闰年"%int(year))
    else:
        if int(year)%4==0:
            print ("%d是闰年" % int(year))
        else:
            print ("%d不是闰年" % int(year))

