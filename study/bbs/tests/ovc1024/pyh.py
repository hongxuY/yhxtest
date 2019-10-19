#encoding:utf-8
import time

class Community():

    url="http://47.92.220.226:8000/bbs2/index.php?app=user&ac=login"
    loginData = {
        u"emalin": u"1459994653@qq.com",
        u"password": u"wo553016"
    }
    def __init__(self,driver):
        self.driver=driver

    def open(self):
        self.driver.get(self.url)


    def login(self):
        self.driver.find_element_by_name(u"email").send_keys(self.loginData[u"emalin"])
        self.driver.find_element_by_name(u"pwd").send_keys(self.loginData[u"password"])
        self.driver.find_element_by_id(u"comm-submit").click()
        time.sleep(5)

    #我的社区
    def myCommunityTest(self):
        # 登录
        self.driver.find_element_by_name(u"email").send_keys(self.loginData[u"emalin"])
        self.driver.find_element_by_name(u"pwd").send_keys(self.loginData[u"password"])
        self.driver.find_element_by_id(u"comm-submit").click()
        time.sleep(5)
        # 点击我的社区
        self.driver.find_element_by_xpath(u"//div[1]/div/a[9]").click()

    #我的小组
    def myCommunity_groupTest(self):
        # 登录
        self.driver.find_element_by_name(u"email").send_keys(self.loginData[u"emalin"])
        self.driver.find_element_by_name(u"pwd").send_keys(self.loginData[u"password"])
        self.driver.find_element_by_id(u"comm-submit").click()
        time.sleep(5)
        # 点击我的社区
        self.driver.find_element_by_xpath(u"//div[1]/div/a[9]").click()
        #点击我的小组
        self.driver.find_element_by_xpath(u"//div[3]/div/div[1]/div/div/div/div[2]/ul[1]/li[2]/a").click()

    #我的文章
    def myCommunity_articleTest(self):
        # 登录
        self.driver.find_element_by_name(u"email").send_keys(self.loginData[u"emalin"])
        self.driver.find_element_by_name(u"pwd").send_keys(self.loginData[u"password"])
        self.driver.find_element_by_id(u"comm-submit").click()
        time.sleep(5)
        # 点击我的社区
        self.driver.find_element_by_xpath(u"//div[1]/div/a[9]").click()
        #点击我的文章
        self.driver.find_element_by_xpath(u"/html/body/div[3]/div/div[1]/div/div/div/div[2]/ul[1]/li[3]/a").click()

    #我的唠叨
    def myCommunity_talkTest(self):
        # 登录
        self.driver.find_element_by_name(u"email").send_keys(self.loginData[u"emalin"])
        self.driver.find_element_by_name(u"pwd").send_keys(self.loginData[u"password"])
        self.driver.find_element_by_id(u"comm-submit").click()
        time.sleep(5)
        # 点击我的社区
        self.driver.find_element_by_xpath(u"//div[1]/div/a[9]").click()
        #点击我的文章
        self.driver.find_element_by_xpath(u"/html/body/div[3]/div/div[1]/div/div/div/div[2]/ul[1]/li[4]/a").click()


