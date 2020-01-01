# encoding:utf-8
import json
import urllib.parse
import requests
import jsonpath
import os
import time

kw = "少女"
kw = urllib.parse.quote(kw)
num = 5
nums = num * 24 + 1
for index in range(0, nums, 24):
    urls = "https://www.duitang.com/napi/blog/list/by_search/?kw=%s&start=%s" % (kw, index)
    resp = requests.get(urls)
    html = json.loads(resp.text)
    photos = jsonpath.jsonpath(html, "$..path")

    dir_name = "D:/test/"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    for url in set(photos):
        time.sleep(1)
        file_name = url.split("/")[-1]
        print(file_name)
        response = requests.get(url)
        with open(dir_name + "/" + file_name, "wb")as f:
            f.write(response.content)
