# ecoding:utf-8
import random
random_num=random.randint(0, 10)
count=0

while True:
    while True:
        try:
            a = int(input('请输入一个数:'))
            break
        except:
            print('请重新输入:')
    count+=1
    if a==random_num:
        print('恭喜你猜对啦,猜了%d次'%count)
        break
    elif a>random_num:
        print('猜大了!')
    elif a<random_num:
        print('猜小了!')