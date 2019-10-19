#encoding:utf-8

import unittest
import requests
import config

class TestMember(unittest.TestCase):
    def test_getAllMember01(self):
        url="http://%s:%s/member"%(config.Host,config.Port)
        resp=requests.get(url)
        resp.encoding="utf-8"
        exp_result = 200
        act_result = resp.status_code
        self.assertEqual(exp_result, act_result,"请求返回正确:exp：%d---act：%d"%(exp_result,act_result))
        jsonData=resp.json()
        print len(jsonData["member"])
        exp_result = int
        act_result = type(jsonData["member"][0]["uid"])
        self.assertEqual(exp_result, act_result)

        exp_result = unicode
        act_result = type(jsonData["member"][0]["tel"])
        self.assertEqual(exp_result, act_result)

        #在Python里，ucs2或者ucs4编码的，我们叫做unicode object
        # 其他编码的我们就叫做string。
        exp_result = unicode
        act_result = type(jsonData["member"][0]["tel"])
        self.assertEqual(exp_result, act_result)

        exp_result = float
        act_result = type(jsonData["member"][0]["discount"])
        self.assertEqual(exp_result, act_result)

        exp_result = int
        act_result = type(jsonData["member"][0]["score"])
        self.assertEqual(exp_result, act_result)

        exp_result = int
        act_result = type(jsonData["member"][0]["active"])
        self.assertEqual(exp_result, act_result)










