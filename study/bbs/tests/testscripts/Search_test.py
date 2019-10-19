# encoding:utf-8

import unittest
from selenium import webdriver
from tests.ovc1024.ovc1024_search import SearchTest
import time

class MyTestCase(unittest.TestCase):
    SearchTest = SearchTest(webdriver)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.SearchTest = SearchTest(cls.driver)
        cls.SearchTest.open()
        user = {
            "username": "1286060621@qq.com",
            "password": "sysr19970911"
        }
        cls.SearchTest.login(user)
        cls.SearchTest.go_to_search()

    def test_search_case01(self):
        self.SearchTest.element_search_input.send_keys(u"我们的目标是永不脱发")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        element_retmsg = self.driver.find_element_by_link_text(u"我们的目标是永不脱发")
        retmsg_text = element_retmsg.text
        act_result = retmsg_text
        exp_result = u"我们的目标是永不脱发"

        self.assertEqual(act_result,exp_result)
        self.SearchTest.element_choose.click()

    def test_search_case02(self):
        self.SearchTest.element_search_input.send_keys(u"213132")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        element_retmsg = self.driver.find_element_by_link_text(u"213132")
        retmsg_text = element_retmsg.text
        act_result = retmsg_text
        exp_result = u"213132"

        self.assertEqual(act_result,exp_result)
        self.SearchTest.element_choose.click()

    def test_search_case03(self):
        self.SearchTest.element_search_input.send_keys(u"华中陈冠希")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        element_retmsg = self.driver.find_element_by_link_text(u"华中陈冠希")
        retmsg_text = element_retmsg.text
        act_result = retmsg_text
        exp_result = u"华中陈冠希"

        self.assertEqual(act_result,exp_result)
        self.SearchTest.element_choose.click()

    def test_search_case04(self):
        self.SearchTest.element_search_input.send_keys(u"386旅独立团团长李云龙")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        element_retmsg = self.driver.find_element_by_link_text(u"386旅独立团团长李云龙")
        retmsg_text = element_retmsg.text
        act_result = retmsg_text
        exp_result = u"386旅独立团团长李云龙"

        self.assertEqual(act_result,exp_result)
        self.SearchTest.element_choose.click()

    def test_search_case05(self):
        self.SearchTest.element_search_input.send_keys(u"我们的目标是永不脱发")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        self.driver.find_element_by_link_text(u"我们的目标是永不脱发").click()
        element_retmsg = self.driver.find_element_by_tag_name(u"h1")
        act_result = element_retmsg.text
        exp_result = u"我们的目标是永不脱发"

        self.assertEqual(act_result,exp_result)
        self.SearchTest.element_choose.click()

    def test_search_case06(self):
        self.SearchTest.element_search_input.send_keys(u"213132")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        self.driver.find_element_by_link_text(u"213132").click()
        element_retmsg = self.driver.find_element_by_tag_name(u"h1")
        act_result = element_retmsg.text
        exp_result = u"213132"

        self.assertEqual(act_result,exp_result)
        self.SearchTest.element_choose.click()

    def test_search_case07(self):
        self.SearchTest.element_search_input.send_keys(u"华中陈冠希")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        self.driver.find_elements_by_link_text(u"华中陈冠希")[1].click()
        element_retmsg = self.driver.find_element_by_tag_name(u"h1")
        act_result = element_retmsg.text
        exp_result = u"华中陈冠希"

        self.assertEqual(act_result,exp_result)
        self.SearchTest.element_choose.click()

    def test_search_case08(self):
        self.SearchTest.element_search_input.send_keys(u"386旅独立团团长李云龙")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        self.driver.find_element_by_link_text(u"386旅独立团团长李云龙").click()
        element_retmsg = self.driver.find_element_by_tag_name(u"h1")
        act_result = element_retmsg.text
        exp_result = u"386旅独立团团长李云龙"

        self.assertEqual(act_result,exp_result)
        self.SearchTest.element_choose.click()

    def test_search_case09(self):
        self.driver.find_element_by_xpath("//body/div[3]/div/div[2]/div/div/div[1]/a[2]")
        self.SearchTest.element_search_input.send_keys(u"我们的目标是永不脱发")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        self.driver.find_element_by_link_text(u"我们的目标是永不脱发").click()
        element_retmsg = self.driver.find_element_by_tag_name(u"h1")
        act_result = element_retmsg.text
        exp_result = u"我们的目标是永不脱发"

        self.assertEqual(act_result,exp_result)
        self.SearchTest.element_choose.click()

    def test_search_case010(self):
        self.driver.find_element_by_xpath("//body/div[3]/div/div[2]/div/div/div[1]/a[3]")
        self.SearchTest.element_search_input.send_keys(u"213132")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        self.driver.find_element_by_link_text(u"213132").click()
        element_retmsg = self.driver.find_element_by_tag_name(u"h1")
        act_result = element_retmsg.text
        exp_result = u"213132"

        self.assertEqual(act_result,exp_result)
        self.SearchTest.element_choose.click()

    def test_search_case011(self):
        self.driver.find_element_by_xpath("//body/div[3]/div/div[2]/div/div/div[1]/a[4]")
        self.SearchTest.element_search_input.send_keys(u"华中陈冠希")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        self.driver.find_element_by_link_text(u"华中陈冠希").click()
        element_retmsg = self.driver.find_element_by_tag_name(u"华中陈冠希")
        act_result = element_retmsg.text
        exp_result = u"华中陈冠希"

        self.assertEqual(act_result, exp_result)
        self.SearchTest.element_choose.click()

    def test_search_case012(self):
        self.driver.find_element_by_xpath("//body/div[3]/div/div[2]/div/div/div[1]/a[5]")
        self.SearchTest.element_search_input.send_keys(u"386旅独立团团长李云龙")
        time.sleep(1)
        self.SearchTest.element_search_button.click()
        self.driver.find_element_by_link_text(u"386旅独立团团长李云龙").click()
        element_retmsg = self.driver.find_element_by_tag_name(u"h1")
        act_result = element_retmsg.text
        exp_result = u"386旅独立团团长李云龙"

        self.assertEqual(act_result, exp_result)
        self.SearchTest.element_choose.click()


if __name__ == '__main__':
    unittest.main()
