# encoding:utf-8
import unittest
import requests
import config
import json
from ddt import ddt, file_data


@ddt
class MyTestcase(unittest.TestCase):

    @file_data("test_get_member_by_uid.json")
    def test_get_member_by_uid(self, uid):
        url = "http://%s:%s/member/uid_%s" % (config.Host, config.Port, uid)
        resp = requests.get(url)
        resp.encoding = "utf-8"
        resp_jsondata = resp.json()
        self.assertEqual(200, resp.status_code), u"请求url:%s,返回状态码：%s" % (url, resp.status_code)
        # print(resp_jsondata['reason'])

        if resp_jsondata['return_code'] == 200:
            exp = 'Get member by uid success'
            act = resp_jsondata['return_msg']
            self.assertEqual(exp, act, 'exp:=%s act:=%s' % (act, exp))
        elif resp_jsondata['return_code'] == 500:
            exp = 'Get member by uid false'
            act = resp_jsondata['return_msg']
            self.assertEqual(exp, act, 'exp:=%s act:=%s' % (act, exp))



if __name__ == '__main__':
    unittest.main()
