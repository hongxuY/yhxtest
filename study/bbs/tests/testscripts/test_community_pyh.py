#encoding:utf-8
import time
import pytest
import unittest
from selenium import webdriver
from tests.ovc1024.pyh import Community

class TestCommunity(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver=webdriver.Firefox()
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.location_page=Community(self.driver)
        self.location_page.open()
    def tearDown(self):
        self.driver.quit()


    def test_login(self):
        self.location_page.login()

        #头像处的用户名
        asc_result = self.driver.find_element_by_xpath(u"//nav/div/div[4]/a")
        #用户名的text
        asc_result=asc_result.text
        exp_result = u"pengyunhao"
        self.assertEqual(exp_result,asc_result)

    # # 将鼠标移到头像处点击我的社区查看能否跳转到我的社区页面
    # def test_ovc1024_case001(self):
    #     loginData = {
    #         u"emalin": u"1459994653@qq.com",
    #         u"password": u"wo553016"
    #     }
    #     my_community=self.location_page.login(loginData)
    #     self.driver.find_element_by_xpath(u"/html/body/nav/div/div[4]/div/ul/li[1]/a").click()
    #     asc_result=self.driver.find_element_by_name(u"我的社区").text
    #     exp_result=u"我的社区"
    #     print asc_result,exp_result
    #     self.assertEqual(exp_result,asc_result)


    #点击我的社区、我的小组(分区)创建小组，能否跳转到小组页面
    def test_myCommunity_case002(self):

        #登录,点击我的社区
        self.location_page.myCommunityTest()
        #点击创建小组
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[1]/div[2]/div[1]/a").click()
        #跳到新窗口
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        #t跳转之后的url
        asc_result=self.driver.current_url
        exp_result=u"http://47.92.220.226:8000/bbs2/index.php?app=group&ac=create"
        self.assertEqual(exp_result,asc_result)


    #点击我的社区、我的小组(分区)点击小组头像,能否跳到对应小组页面

    def test_myCommunity_case003(self):
        # 登录,点击我的社区
        self.location_page.myCommunityTest()
        #小组名称
        exp_result=self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[1]").text
        # 点击小组头像
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[1]/div[2]/div[2]/div/div/a/img").click()
        #加载之后的小组名称
        asc_result=self.driver.find_element_by_xpath(u"//div[3]/div[1]/div[1]/div/div[1]/div/div/h1").text
        self.assertEqual(exp_result,asc_result)

    #点击我的社区、我的小组(分区)能否查看已加入的小组
    def test_myCommunity_case004(self):
        # 登录,点击我的社区
        self.location_page.myCommunityTest()
        #已加入的小组
        asc_result=self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[1]/div[2]/div[1]/div").text
        exp_result=u"已加入1个小组"
        self.assertEqual(exp_result,asc_result)

    #点击我的社区、我的小组(分区)发帖，能否跳转到小组发帖页面
    def test_myCommunity_case005(self):
        # 登录,点击我的社区
        self.location_page.myCommunityTest()
        #点击发帖
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/a").click()
        #发帖页面的url
        asc_result=self.driver.current_url
        exp_result=u"http://47.92.220.226:8000/bbs2/index.php?app=group&ac=add&id=41"
        self.assertEqual(exp_result,asc_result)

    #点击我的社区、我的贴子(分区)、贴子标题，能否跳转到贴子页面
    def test_myCommunity_case006(self):
        # 登录,点击我的社区
        self.location_page.myCommunityTest()
        #跳转贴子页面
        self.driver.find_element_by_xpath("//div[3]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/a").click()
        asc_result=self.driver.current_url
        exp_result=u"http://47.92.220.226:8000/bbs2/index.php?app=group&ac=topic&id=5"
        self.assertEqual(exp_result,asc_result)

    #点击我的社区、我的贴子(分区)能否进行修改操作并跳到帖子修改页面
    def test_myCommunity_case007(self):
        # 登录,点击我的社区
        self.location_page.myCommunityTest()
        #跳转修改贴子
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[4]/a").click()
        asc_result = self.driver.current_url
        exp_result=u"http://47.92.220.226:8000/bbs2/index.php?app=group&ac=topicedit&topicid=5"

    #点击我的社区、我的文章(分区)能否进行修改操作并跳到文章修改文章页面
    def test_myCommunity_case008(self):
        # 登录,点击我的社区
        self.location_page.myCommunityTest()
        #跳转我的文章页面
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[3]/div[2]/table/tbody/tr/td[4]/a").click()
        asc_result = self.driver.current_url
        exp_result=u"http://47.92.220.226:8000/bbs2/index.php?app=article&ac=edit&articleid=15"
        self.assertEqual(exp_result,asc_result)
    #点击我的社区、我的小组，查看创建的小组是否能看到自己所创建的小组
    def test_myCommunity_case009(self):
        # 点击登录、我的社区、我的小组
        self.location_page.myCommunity_groupTest()
        #查看小组名称
        asc_result=self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div").text
        exp_result=u"pyh"
        self.assertEqual(exp_result,asc_result)


    #点击我的社区、我的小组，查看创建的小组的小组图标是否可以点击并跳转到小组页面
    def test_myCommunity_case010(self):
        # 点击登录、我的社区、我的小组
        self.location_page.myCommunity_groupTest()
        #小组名称
        exp_result = self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div").text
        # 点击小组头像
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[1]/div[2]/div/div/div/a/img").click()
        # 加载之后的小组名称
        asc_result = self.driver.find_element_by_xpath(u"/html/body/div[3]/div[1]/div[1]/div/div[1]/div/div/h1").text
        self.assertEqual(exp_result, asc_result)


    #点击我的社区、我的小组，查看创建的小组能否点击管理并跳转到小组设置页面
    def test_myCommunity_case011(self):
        # 点击登录、我的社区、我的小组
        self.location_page.myCommunity_groupTest()
        #管理小组
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/p/a").click()
        asc_result=self.driver.current_url
        exp_result=u"http://47.92.220.226:8000/bbs2/index.php?app=group&ac=edit&ts=base&groupid=41"
        self.assertEqual(exp_result,asc_result)

    #点击我的社区、我的小组页面能否查看加入的小组
    def test_myCommunity_case012(self):
        # 点击登录、我的社区、我的小组
        self.location_page.myCommunity_groupTest()
        #查看加入的小组名称
        asc_result=self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/div").text
        exp_result=u"pyh"
        self.assertEqual(exp_result,asc_result)

    #点击我的社区、加入的小组小组头像是否可以点击并跳转到小组页面
    def test_myCommunity_case013(self):
        # 点击登录、我的社区、我的小组
        self.location_page.myCommunity_groupTest()
        #小组名称
        exp_result = self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/div").text
        # 点击小组头像
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[2]/div[2]/div/div/div/a/img").click()
        # 加载之后的小组名称
        asc_result = self.driver.find_element_by_xpath(u"//div[3]/div[1]/div[1]/div/div[1]/div/div/h1").text
        self.assertEqual(exp_result, asc_result)

    #点击我的社区、加入的小组在加入的小组中发帖是否能跳转到小组发帖页面
    def test_myCommunity_case014(self):
        # 点击登录、我的社区、我的小组
        self.location_page.myCommunity_groupTest()
        # 点击管理小组
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/p/a").click()
        asc_result = self.driver.current_url
        exp_result = u"http://47.92.220.226:8000/bbs2/index.php?app=group&ac=add&id=41"
        self.assertEqual(exp_result, asc_result)

    #点击我的社区、我的文章页面能否发布文章并跳转到文章 / 修改文章页面
    def test_myCommunity_case015(self):
        # 点击登录、我的社区、我的文章
        self.location_page.myCommunity_articleTest()
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div/div[2]/div[1]/a").click()
        # 跳到新窗口
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #跳转之后的url
        asc_result = self.driver.current_url
        exp_result=u"http://47.92.220.226:8000/bbs2/index.php?app=article&ac=add"
        self.assertEqual(exp_result,asc_result)


    #点击我的社区、我的文章页面能否查看已发布多少篇文章
    def test_myCommunity_case016(self):
        # 点击登录、我的社区、我的文章
        self.location_page.myCommunity_articleTest()
        #已发布N篇文章
        asc_result=self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div/div[2]/div[1]").text
        exp_result=u"已发布1篇文章"
        self.assertIn(exp_result,asc_result)

    #点击我的社区、我的文章能否对文章进行删除操作，并提示是否删除
    def test_myCommunity_case017(self):
        # 点击登录、我的社区、我的文章
        self.location_page.myCommunity_articleTest()
        #点击删除
        self.driver.find_element_by_xpath(u"/html/body/div[3]/div/div[2]/div/div[2]/table/tbody[1]/tr/td[3]/a[2]").click()
        try:
            #有弹窗
            alert = self.driver.switch_to.alert
            alert.accept()
            asc_result= True
        except:
            print "没有弹窗存在"
            asc_result= False

        exp_result=False
        #OK表示没有弹窗提示，报错表示有
        self.assertEqual(asc_result,exp_result)

    #点击我的社区、我的唠叨(输入内容)、发布，是否可以发布并跳转到唠叨页面
    def test_myCommunity_case018(self):
        # 点击登录、我的社区、我的唠叨
        self.location_page.myCommunity_talkTest()
        #输入内容
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div/div[2]/div[1]/form/textarea").send_keys(u"aa")
        #点击发布
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div/div[2]/div[1]/form/div/button").click()
        #取一个跳转之后的页面元素的text
        asc_result=self.driver.find_element_by_xpath(u"/html/body/div[3]/nav/ol/li[2]/a").text

        exp_result = u"唠叨"
        self.assertEqual(exp_result, asc_result)

    #点击我的社区、我的唠叨、回复是否能跳转的唠叨页面
    def test_myCommunity_case019(self):
        # 点击登录、我的社区、我的唠叨
        self.location_page.myCommunity_talkTest()
        #点击回复
        self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div/div[2]/div[3]/ul/li[2]/p/a").click()
        #查找新页面的一个元素的text
        asc_result=self.driver.find_element_by_xpath(u"//div[3]/div/div[1]/div[2]/div[2]/form/div/button").text
        exp_result=u"回复"
        self.assertEqual(exp_result,asc_result)


if __name__ == '__main__':
    unittest.main()
