import unittest
import requests

class MyTestCase(unittest.TestCase):
    def test_something(self):
        url="http://127.0.0.1:5000/"
        data= {"username": "yuan", "password": 123}
        resp=requests.post(url,data)
        resp=resp.json()
        print(resp)
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
