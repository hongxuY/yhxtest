# encoding:utf-8
import requests
from bs4 import BeautifulSoup
import os
import time
import re

url = "https://www.vmgirls.com/9472.html"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

response = requests.get(url, headers=headers)
# print(response.text)
# soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")
# 获取所有的链接
# links = soup.find_all('a')
# print("所有的链接")
# for link in links:
#     print(link.name, link['href'], link.get_text())
#
#     print("获取特定的URL地址")
#     link_node = soup.find('a', href="http://example.com/elsie")
#     print(link_node.name, link_node['href'], link_node['class'], link_node.get_text())
#
#     print("正则表达式匹配")
#     link_node = soup.find('a', href=re.compile(r"ti"))
#     print(link_node.name, link_node['href'], link_node['class'], link_node.get_text())
#
#     print("获取P段落的文字")
#     p_node = soup.find('p', class_='story')
#     print(p_node.name, p_node['class'], p_node.get_text())

html = response.text
print(html)
dir_name = "D:/test/" + str(re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[0])
urls = re.findall('<img alt=".*?" src=".*?" width=".*?" height=".*?" class=".*?" data-src="(.*?)" data-nclazyload=".*?" data-srcset=".*?" data-sizes=".*?">', html)
print(dir_name)
print(urls)
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
for url in set(urls):
    time.sleep(1)
    file_name = url.split("/")[-1]
    print(file_name)
    response = requests.get(url, headers=headers)
    with open(dir_name + "/" + file_name, "wb")as f:
        f.write(response.content)
