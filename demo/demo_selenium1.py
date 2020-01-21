# coding:utf-8
from selenium import webdriver
import time

# 启动火狐浏览器
driver = webdriver.Firefox()
driver.implicitly_wait(10)
# 打开url
driver.get("https://whiot.ihaozhuo.com/msjPage/index.html#/login")
time.sleep(2)

driver.find_element_by_xpath('//*[@id="tab-second"]').click()
driver.find_element_by_xpath('//*[@id="pane-second"]/div/form/div[1]/div/div[1]/div/input').send_keys('15611111111')
driver.find_element_by_xpath('//*[@id="pane-second"]/div/form/div[2]/div/div[1]/div[2]/input').send_keys('123456')
driver.find_element_by_xpath('//*[@id="pane-second"]/div/div/button/span').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/ul/div/li[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div[1]/ul/div/li[1]/ul/a[2]/li/span').click()

print(driver.current_url)
print(driver.title)
driver.close()
