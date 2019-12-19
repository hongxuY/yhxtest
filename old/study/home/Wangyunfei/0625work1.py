# coding:utf-8
while True:
    try:
        a=int(input('请输入一个年份'))
        if a<0:
            print('不可为负数')
            break
    except:
        print('请重新输入')

if int(a) % 100 == 0:
    if int(a) % 400 == 0:
        print ("%d是闰年" % a)
    else:
        print ("%d不是闰年" % a)
else:
    if int(a) % 4 == 0:
        print ("%d是闰年" % a)
    else:
        print ("%d不是闰年" % a)








