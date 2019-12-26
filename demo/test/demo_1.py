# coding:utf-8
import os
import requests
import time
import re

wangzhi = "https://www.vmgirls.com/13344.html"


def pa(wangzhi):
    try:
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
        requests.packages.urllib3.disable_warnings()
        resp = requests.get(wangzhi, verify=False, headers=header)
        # print(resp.text)
        html = resp.text

        dir_name = "D:/test/" + str(re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[0])
        urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
        # print(dir_name)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        for url in urls:
            time.sleep(2)
            file_name = url.split("/")[-1]
            resp = requests.get(url, verify=False, headers=header)
            with open(dir_name + "/" + file_name, "wb")as f:
                f.write(resp.content)

        print(dir_name.split("/")[-1] + ":获取成功")
    except:
        print(wangzhi + "获取失败")


pa(wangzhi)
