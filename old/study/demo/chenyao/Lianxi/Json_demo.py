# encoding:utf-8

str = "[{'discount': 0.95, 'tel': '18812345672', 'id': '1'}, {'discount': 0.9, 'tel': '18812345673', 'id': '2'}, {'discount': 0.9, 'tel': '18812345674', 'id': '3'}, {'discount': 0.8, 'tel': '18812345671', 'id': '4'}, {'discount': 0.8, 'tel': '18811345671', 'id': '5'}]"

dic = {"resultcode": "200", "reason": "Return Successd!",
       "result": {"province": "浙江", "city": "杭州", "areacode": "0571", "zip": "310000", "company": "移动", "card": ""},
       "error_code": 0}

members_count = str.count('id')
print(members_count)

tel_list = str.split('[{')[-1].split('}]')[0].split('}, { ')
# print(tel_list)
for tel in tel_list:
    tel_mem = tel.split(',')[1].split('\'')[3]
    print(tel_mem)
# print(tel_list)

c = dic["result"]
print ('省份：%s\n城市：%s\n公司：%s\n' % (c["province"], c["city"], c["company"]))
# print (c["province"])
