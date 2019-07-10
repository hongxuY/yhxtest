# -*- encoding:utf-8 -*-

import unittest
import requests
from ddt import ddt, file_data
import config


@ddt
class MyTestCase(unittest.TestCase):
    @file_data("test_addRegister.json")
    def test_testTel(self,tel):
        url ="http://%s:%s/member"%(config.Host,config.Port)
        payload = {
            "tel":tel
        }
        resp = requests.post(url,data=payload)
        resp.encoding = "utf-8"

        resp_jsondata = resp.json()
        print(resp_jsondata["return_code"])


if __name__ == '__main__':
    unittest.main()