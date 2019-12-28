# coding:utf-8
import requests
import re

url = "http://pic.netbian.com/4kdongman/"
headers = {

}
respson = requests.get(url)
respson.encoding = respson.apparent_encoding
print(respson.text)

# respson_text = respson.text
# urls = re.findall('<a href=(.*?)>', respson_text)
#
# for i in urls:
#     print(i)
