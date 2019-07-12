#encoding:utf-8
from selenium import webdriver
import json
driver= webdriver.Firefox()

url="http://47.92.220.226/webdriver/"
driver.get(url)

# eles=driver.find_element_by_link_text(u'定位方法测试页面')
# eles.click()
eles = driver.find_element_by_partial_link_text(u'测试页面')
eles.click()

input_name=driver.find_element_by_id(u'username')
input_name.send_keys(u'yanzhenxing')
input_email=driver.find_element_by_name(u'email')
input_email.send_keys(u'1234@qq.com')
# input_password=driver.find_elements_by_class_name(u'login_input')[2]
# input_password.send_keys(u'1233')
input_password=driver.find_element_by_id(u'password')
input_password.send_keys('1233')
input_twopwd=driver.find_element_by_css_selector(u'#confirm_password')
input_twopwd.send_keys(u'1233')
denglu=driver.find_element_by_xpath(u'//td[@colspan]/input[1]')
denglu.click()

# ret_msg=driver.find_element_by_id(u'regmsg')
# ret_msg_text=ret_msg.text
# ret_msg_json=json.loads(ret_msg_text.split(u'成功')[-1],encoding='utf-8')
#
# print('uid:%s'%(ret_msg_json['uid']))
#通过ID获取返回值显示页面元素
ele_regmsg = driver.find_element_by_id(u"regmsg")
regmsg_text = ele_regmsg.text
regmsg_json = json.loads(regmsg_text.split(u"成功:")[-1], encoding='utf-8')

print("uid: %s" % regmsg_json['uid'])
print("username: %s" % regmsg_json['username'])
print("password: %s" % regmsg_json['password'])
print("email: %s" % regmsg_json['email'])