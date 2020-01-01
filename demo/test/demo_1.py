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
        html = resp.text
        dir_name = "D:/test/" + str(re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[0])
        urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
        # print(dir_name)
        if len(urls) != 0:
            print(dir_name + ":使用方式一获取成功")
        else:
            urls = re.findall(
                '<img alt=".*?" src=".*?" width=".*?" height=".*?" class=".*?" data-src="(.*?)" data-nclazyload=".*?" data-srcset=".*?" data-sizes=".*?">',
                html)
        if len(urls) == 0:
            print(dir_name + wangzhi + "获取失败")
            return "lose"
        print(urls)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        for url in set(urls):
            time.sleep(2)
            file_name = url.split("/")[-1]
            resp = get_request(url)
            with open(dir_name + "/" + file_name, "wb")as f:
                f.write(resp.content)
        return (dir_name.split("/")[-1] + ":成功获取")
    except:
        print(wangzhi + "获取失败")
        return None


def get_photo(num):
    for i in range(20):
        if i == 0:
            wang = "https://www.vmgirls.com/" + num + ".html"
        else:
            wang = "https://www.vmgirls.com/" + num + "/page-" + str(i + 1) + ".html"
        aa = pa(wang)
        if aa == None:
            print("获取到最后一页了")
            break
        elif aa == "lose":
            break
        else:
            print(aa + "第%d页" % (i + 1))


nums = ['10990', '12105', '10777', '12543', '10788', '11745', '10766', '12570', '11221', '11242', '10870', '11153',
        '12487', '10754', '13322', '11075', '11839', '12210', '12163', '11818', '13055', '11062', '10800', '11015',
        '11046', '11208', '13124', '10814', '12691', '11375', '11232', '9887', '9472', '9924', '3851', '3903', '9534',
        '3861', '3877', '3831', '9821', '9873', '9334', '3830', '9765', '9840', '9914', '9081', '3846', '10442',
        '12901', '11784', '9744', '9869', '3825', '3824', '12825', '12279', '3906', '9809', '12210', '11327', '10564',
        '3893', '3836', '3874', '11931', '3818', '3886', '9635', '9408', '9351', '3890', '12353', '10106', '12082',
        '9512', '9445', '10062', '3866', '9049', '9028', '3839', '9964', '12925', '9402', '3838', '9384', '3892',
        '3844', '3852', '10100', '9783', '9412', '3872', '9494', '11410', '3865', '3905', '3898', '10317', '10528',
        '3826', '3876', '3858', '9568', '8896', '3867', '10080', '8908', '3837', '3907', '9588', '9523', '3860', '3888',
        '10070', '10369', '3899', '10091', '9036', '9953', '12122', '12333', '10034', '3883', '3863', '3822', '9666',
        '3859', '10052', '9483', '10032', '3875', '3854', '10255', '9065', '9224', '9651', '8920', '3849', '3895',
        '12536', '12530', '3827', '9622', '10589', '3864', '3902', '9090', '3904', '3894', '3869', '3891', '10086',
        '3889', '11232', '13172', '3868', '3819', '9699', '9456', '11707', '3897', '9550', '3896', '3901']
for num in nums:
    print(num)
    get_photo(num)

# wangzhi = "https://www.vmgirls.com/wp-admin/admin-ajax.php"
# query = 17
# num_list = []
# for i in range(1, query + 1):
#     # data = {
#     #     "append": "list-archive",
#     #     "paged": i,
#     #     "action": "ajax_load_posts",
#     #     "query": query,
#     #     "page": "cat"
#     # }
#     data = {
#         "append": "list-home",
#         "paged": i,
#         "action": "ajax_load_posts",
#         "query": "",
#         "page": "home"
#     }
#     resp = post_request(wangzhi, data)
#     time.sleep(1)
#     html = resp.text
#     nums = re.findall('<a href="(.*?)">', html)
#
#     for n in set(nums):
#         num = re.findall('https://www.vmgirls.com/(.*?).html', n)
#         if num == []:
#             break
#         else:
#             num_list.append(num[0])
#
# print(set(num_list))
#
# for i in set(num_list):
#     get_phtot(i)
