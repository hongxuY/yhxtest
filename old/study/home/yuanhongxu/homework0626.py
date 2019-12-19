#coding:utf-8

import random

random_number=random.randint(0,100)
print (random_number)
count=0
while True:
    try:
        count += 1
        number=input("请输入你猜的数值")
        if isinstance(number,float):
            print ("不能输入小数")
        elif number==count:
            print("输入错误，请重新输入")
        elif number==random_number:
            print ("恭喜你猜对了，猜了%d次"%(count))
            break
        elif number>random_number:
            print ("猜大了")
        else:
            print ("猜小了")
    except:
        print ("输入错误，请重新输入")






