# encoding:utf-8

rembers = [
    {'id':'1','tel':'18812345671','discount':'0.98'},
    {'id':'2','tel':'18812345672','discount':'0.9'},
    {'id':'3','tel':'18812345673','discount':'0.8'}
]
tel = '18812345672'
for rember in rembers:
    if rember['tel']==tel:
        print(rember['discount'])
