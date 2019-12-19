#encoding:utf-8
#这个程序有一个BUG，当输入的值与计数器的变量名称相同是会有问题，但是不知道怎么解决
import random
i=random.randint(0,100)
print(i)
a=0
while True:

    while True:
          try:
              c=int(input("请输入猜测的数字:\n"))
              break

          except:
              print("输入有误，请重新输入！")
    a+=1
    if c==i:
        print("猜对了！一共猜了%d"%a)
        break
    elif c<i:
        print("猜小了！")
    elif c>i:
        print("猜大了！")