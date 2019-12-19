# encoding:utf-8

import unittest
import requests
from ddt import ddt, file_data
import config


@ddt
class TestUidLocation(unittest.TestCase):
    @file_data("test_Delete_member_by_uid.json")
    def test_testUid(self, input_data):
        url = "http://%s:%s/member/uid_%s" % (config.Host, config.Port, input_data["uid"])

        resp = requests.delete(url, data=input_data["uid"])
        resp.encoding = "utf-8"

        self.assertEqual(200, resp.status_code, u'请求url:%s,响应状态码:%s' % (url, resp.status_code))
        resp_jsondata = resp.json()
        print (resp_jsondata)

        if resp_jsondata['ret_code'] == 200:
            expect = {
                "uid": input_data["uid"],
                "tel": resp_jsondata['tel'],
                "discount": 1,
                "active": 0,
                "score": resp_jsondata['score']
            }
            exp = expect
            act = {
                "uid": input_data["uid"],
                "tel": resp_jsondata['tel'],
                "discount": 1,
                "active": 0,
                "score": resp_jsondata['score']
            }
            self.assertEqual(exp, act, 'exp:%s act:%s' % (act, exp))

        else:
            exp = 'delete user false'
            act = resp_jsondata['ret_msg']
            self.assertEqual(exp, act, 'exp:%s act:%s' % (act, exp))

if __name__ == '__main__':
        unittest.main()
