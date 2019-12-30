# coding:utf-8
import os
import requests
import time
import re

def get_request(wangzhi):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    requests.packages.urllib3.disable_warnings()
    resp = requests.get(wangzhi, verify=False, headers=header)
    return resp


def post_request(wangzhi, data):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    requests.packages.urllib3.disable_warnings()
    resp = requests.post(wangzhi, data, verify=False, headers=header)
    return resp


def pa(wangzhi):
    try:
        resp = get_request(wangzhi)
        # print(resp.text)
        # return None
        html = resp.text

        dir_name = "D:/test/" + str(re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[0])
        urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
        # print(dir_name)
        if len(urls)==0:
            return None
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        for url in urls:
            time.sleep(2)
            file_name = url.split("/")[-1]
            resp = get_request(url)
            with open(dir_name + "/" + file_name, "wb")as f:
                f.write(resp.content)

        return (dir_name.split("/")[-1] + ":成功获取")
    except:
        print(wangzhi + "获取失败")
        return None


def get_phtot(num):
    for i in range(20):
        if i == 0:
            wang = "https://www.vmgirls.com/" + num + ".html"
        else:
            wang = "https://www.vmgirls.com/" + num + "/page-" + str(i + 1) + ".html"
        aa = pa(wang)
        if aa == None:
            print("获取到最后一页了")
            break
        else:
            print(aa + "第%d页" % (i + 1))

nums={'10990', '12105', '10777', '12543', '10788', '11745', '10766', '12570', '11221', '11242', '10870', '11153', '12487', '10754', '13322', '11075', '11839', '12210', '12163', '11818', '13055', '11062', '10800', '11015', '11046', '11208', '13124', '10814', '12691', '11375', '11232'}
for num in nums:
    get_phtot(num)

wangzhi = "https://www.vmgirls.com/wp-admin/admin-ajax.php"
query = 17
num_list = []
for i in range(1, query + 1):
    # data = {
    #     "append": "list-archive",
    #     "paged": i,
    #     "action": "ajax_load_posts",
    #     "query": query,
    #     "page": "cat"
    # }
    data = {
        "append": "list-home",
        "paged": i,
        "action": "ajax_load_posts",
        "query": "",
        "page": "home"
    }
    resp = post_request(wangzhi, data)
    time.sleep(1)
    html = resp.text
    nums = re.findall('<a href="(.*?)">', html)

    for n in set(nums):
        num = re.findall('https://www.vmgirls.com/(.*?).html', n)
        if num == []:
            break
        else:
            num_list.append(num[0])

# print(set(num_list))

# for i in set(num_list):
#     get_phtot(i)
