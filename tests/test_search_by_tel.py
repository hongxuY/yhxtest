#encoding:utf-8
import  unittest
import config
import  json
import  requests
from  ddt import ddt,file_data


@ddt
class TestMemByTel(unittest.TestCase):

    @file_data("test_search_by_tel.json")
    def test_SearchByTel(self,tel):
        url="http://%s:%s/member" % (config.Host, config.Port)
        payload={
            "tel":tel
        }
        resp=requests.get(url,params=payload)
        resp.encoding="utf-8"

        resp_jsondata=resp.json()
        print(resp_jsondata)
        # 怎加对500的验证，如果失败，直接返回断言结果
        self.assertEqual(200,resp.statue_code,"请求url:%s,返回状态码%s"%(url,resp("statue_code")))
        if resp_jsondata["resp.text"]==200:
            esp_result='search mem by tel success!'
            act_result = resp_jsondata['ret_msg']
            self.assertEqual(esp_result,act_result,  'exp:%s act:%s' % (act_result, esp_result))
        elif resp_jsondata["resp.text"]==400:
            esp_result = 'search mem by tel failed!'
            act_result = resp_jsondata['ret_msg']
            self.assertEqual(esp_result, act_result, 'exp:%s act:%s' % (act_result, esp_result))