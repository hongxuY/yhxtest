#encoding:utf-8
import unittest
import requests
from ddt import ddt,file_data
import config

@ddt
class TestUpdateScore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up test case")

    @classmethod
    def tearDownClass(cls):
        print("tear down test case")

    @file_data("test_updatescore_by_uid.json")
    def test_UpdateScore(self,input_data,expect_data):
        url="http://%s:%s/member/uid_%s"%(config.Host,config.Port,input_data["uid"])
        payload={
                "score":input_data["score"],
 }
        resp=requests.patch(url,data=payload)
        resp.encoding="utf-8"
        resp_data = resp.json()
        self.assertEqual(200,resp.status_code,u"请求url:%s,返回状态码：%s"%(url,resp.status_code))
        if input_data["score"] > 0 or input_data["score"] == 0 and isinstance(input_data["score"], int):
            resp_data["score_before"]=0
            resp_data["score_after"]=200
        fail_list = []
        for key in expect_data.keys():
            try:
                # 判断判断响应体中键对应的值不匹配
                if expect_data[key] != resp_data[key]:
                    fail_list.append(key)
            except:
                # 判断响应体中不存在指定的键
                fail_list.append(key)
        self.assertEqual(0, len(fail_list),"exp_json:%s, act_json:%s, failed_keys:%s" % (str(expect_data), str(resp_data), str(fail_list)))



if __name__ == '__main__':
    unittest.main()

