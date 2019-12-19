# encoding:utf-8
import random
number = random.randint(0,100)
count=0
while True:
    try:
        num=int(input('请输入一个数字:'))
    except:
        print "请输入一个0-100的整数:"
        continue
    if num==number:
        count=count+1
        print ('恭喜你猜对了，一共猜了%d 次'%count)
        break
    elif num>number:
        print "猜大了"
    else:
        count=count+1
        print "猜小了"
