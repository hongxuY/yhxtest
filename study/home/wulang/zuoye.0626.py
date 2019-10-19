# encoding:utf-8
import random
random_numer = random.randint(0,100)
print(random_numer)
count = 0

while True:
    while True:
        try:
            a = int(input('请输入一个数:'))
            break
        except:
            print('请重新输入:')
    count += 1
    if a == random_numer:
        print('恭喜你猜对啦,猜了%d次'%count)
        break
    elif a > random_numer:
        print('猜大了!')
    elif a < random_numer:
        print('猜小了!')

















