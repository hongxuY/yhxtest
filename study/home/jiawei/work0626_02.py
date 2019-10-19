#encoding:utf-8
while True:
    try:
      y=int(input("请输入年份："))
      break
    except :
        print("请输入合法的年份！")

if y<0:
    print("年份不能为负数！")
elif y%4==1 or y%4==2 or y%4==3:
    print("%d是普通年份"%y)
elif y%4==0 and y%100!=0:
    print("%d是普通闰年"%y)
elif y%400==0:
    print("%d是世纪闰年"%y)
