# coding:utf-8


members=[
    {"id":"1","tel":"18902371234","discount":0.80},
    {"id":"2","tel":"18302531239","discount":0.90},
    {"id":"3","tel":"13503321236","discount":0.95},
    {"id":"4","tel":"12590178902","discount":0.98}
]

for i in members:
    print(type(i))
    print (i["tel"])
    print(type(i["tel"]))
    b = list(i["tel"])
    print(b)
    print (b[7:11])


for i in members:
      jifen=int(raw_input("请输入用户积分："))
      i["jifen"]=jifen
      print(type(i["jifen"]))

