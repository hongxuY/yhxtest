# encoding:utf-8
members = [
    {'id': '1', 'tel': '13112345678', 'disc':0.9},
    {'id': '2', 'tel': '13212345678', 'disc': 0.95},
    {'id': '3', 'tel': '13312345678', 'disc': 0.8},
    {'id': '4', 'tel': '13412345678', 'disc': 0.7},
    {'id': '5', 'tel': '13512345678', 'disc': 0.85},
    {'id': '6', 'tel': '13612345678', 'disc': 0.75},
    {'id': '7', 'tel': '13712345678', 'disc': 0.65},
]

#新增
a = {'id':'8','tel':'13812345678','disc':0.9}
members.append(a)
print (members)

#获取所有会员列表
for mem in members:
    print ("会员编号：%s  \t电话:%s\t折扣:%s折\t" % (mem['id'], mem['tel'], mem['disc']))

#根据手机号后四位获取会员信息。
