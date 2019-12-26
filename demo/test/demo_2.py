# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.vmgirls.com/")

time.sleep(5)

links = driver.find_elements_by_tag_name("a")

for link in links:
    a = link.get_attribute("href")
    print(a)

driver.close()
