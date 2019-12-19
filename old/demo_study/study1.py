# -*- coding: UTF-8 -*-

#x的三次方的数据的列表
num=[x ** 3 for x in range(5)]

for i in num:
    print(i)

print("============================================")


#x的二次方的数据的列表去掉最终数据为2的倍数的数据
num=[x ** 2 for x in range(8) if not x % 2]

for i in num:
    print(i)


