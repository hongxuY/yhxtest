# encoding:utf-8

import random
random_num=random.randint(0,101)
c=0
while True:
    while True:
        try:
            b=int(input("输入一个数字来玩游戏"))
            break

        except:
            print("请重新输入：")
    a=random_num
    c+=1
    if b==a:
        print("恭喜你猜对了，猜了%d次"%c)
    elif b>a:
        print("你猜大了")
    else:
        print("你猜小了")




