# encoding:utf-8
year = int(input("请输入一个年份："))
if year %4 == 0 and year %4!=0:
    print("该年份为普通闰年")
elif year % 400 == 0:
    print("该年份是世纪闰年")
else:
    print("该年份不是闰年")