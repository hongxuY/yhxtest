# encoding:utf-8
import requests
import os
import time
import re


def get_photo2(num):
    url = "https://www.vmgirls.com/" + num + ".html"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    html = response.text
    # print(html)
    dir_name = "D:/test/" + str(re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[0])
    urls = re.findall(
        '<img alt=".*?" src=".*?" width=".*?" height=".*?" class=".*?" data-src="(.*?)" data-nclazyload=".*?" data-srcset=".*?" data-sizes=".*?">',
        html)
    print(dir_name)
    if len(urls) != 0:
        print(dir_name + ":使用方式二获取成功")
    else:
        return "lose"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    for url in set(urls):
        time.sleep(1)
        file_name = url.split("/")[-1]
        print(file_name)
        response = requests.get(url, headers=headers)
        with open(dir_name + "/" + file_name, "wb")as f:
            f.write(response.content)


print(get_photo2("9472"))
