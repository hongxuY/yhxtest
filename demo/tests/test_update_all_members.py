# -*- encoding:utf-8 -*-
import unittest
import requests
from ddt import ddt, file_data
from demo.tests import config


@ddt
class MyTestCase(unittest.TestCase):
    @file_data("test_update_all_members.json")
    def test_update_all_members(self, input_data, expect_data):
        url = "http://%s:%s/member/uid_%s" % (config.Host, config.Port, input_data["uid"])
        payload = {}
        for key in input_data.keys():
            if input_data[key]!=None:
                payload[key] = input_data[key]
        # if input_data["active"] != None:
        #     payload["active"] = input_data["active"]
        # if input_data["score"] != None:
        #     payload["score"] = input_data["score"]
        # if input_data["discount"] != None:
        #     payload["discount"] = input_data["discount"]
        # if input_data["tel"] != None:
        #     payload["tel"] = input_data["tel"]
        resp = requests.put(url, data=payload)
        resp.encoding = "utf-8"
        self.assertEqual(200, resp.status_code, u"请求url：%s，返回码%s" % (url, resp.status_code))
        resp_data = resp.json()
        fail_list = []
        for key in expect_data.keys():
            try:
                if resp_data[key] != expect_data[key]:
                    fail_list.append(key)
            except:
                fail_list.append(key)
        print (resp_data)
        print (expect_data)
        print (fail_list)
        self.assertEqual(len(fail_list), 0)


if __name__ == '__main__':
    unittest.main()
