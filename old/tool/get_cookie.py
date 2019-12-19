# coding:utf-8
from selenium import webdriver
import time
import json


# 获取cookie
driver = webdriver.Firefox()
driver.get("https://hz.ihaozhuo.com:5443/#/")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="userName"]').send_keys("15623219550")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("yuan123")
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div[1]/form/button').click()

cookies = driver.get_cookies()
print(type(cookies))
# print ("".join(cookies))
f1 = open('cookie.txt', 'w')
f1.write(json.dumps(cookies))
f1.close()

# 读取cookie
f1 = open('cookie.txt')
cookie = f1.read()
cookie =json.loads(cookie)
for c in cookie:
    driver.add_cookie(c)
# # 刷新页面
driver.refresh()