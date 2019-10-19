#encoding:utf-8
while 1:
    try:
        i=int(input("请输入年份:"))
        if i % 4 == 0 and i % 100 != 0:
            print("%d是闰年" % (i))
            break
        elif i % 400 == 0:
            print ("%d是世纪闰年" % (i))
            break
        else:
            print ("%d不是闰年" % (i))
            break
    except:
        print
        print ("输入错误请输入年份")