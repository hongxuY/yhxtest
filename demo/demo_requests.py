# coding:utf-8
import requests
import os

# url = "https://whiot.ihaozhuo.com/msjPage/index.html#/accountmanagement/dataReport"
# response = requests.get(url)
# response.encoding = response.apparent_encoding
# print(response)
# print(type(response))
# print(response.text)

url1 = "https://whiot.ihaozhuo.com/qrhealth/manage/managequertgoods"
header = {"Cookie": "token=MTQzMDAwMTAwMDE="}
data = {
    "goodtype": "全部",
    "goodname": "",
    "instname": "",
    "goodputaway": "全部",
    "page": 1,
    "pagesize": 10,
    "goodid": "",
    "creatpeople": "",
    "creatpeoplename": ""
}
response1 = requests.post(url1, data, headers=header)
print(response1.text)
