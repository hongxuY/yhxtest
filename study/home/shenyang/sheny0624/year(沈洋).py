#coding:UTF-8

a=int(input("输入年份为："))
if a%4==0 and a%100!=0:
    print("此年份为普通闰年")
elif a%400==0:
    print("此年份为世纪闰年")
else:
    print("此年分不是闰年")