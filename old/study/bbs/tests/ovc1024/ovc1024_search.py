# encoding:utf-8
import time

class SearchTest():

    url="http://47.92.220.226:8000/bbs2/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def login(self,user):
        self.element_longin.click()
        self.element_username.send_keys(user["username"])
        self.element_password.send_keys(user["password"])
        self.element_submit.click()

    @property
    def element_longin(self):
        element = self.driver.find_element_by_xpath(u'//div[@class="ts-user-nav"]/a[1]')
        return element

    @property
    def element_username(self):
        element = self.driver.find_element_by_xpath(u"//body/div[3]/div/div[2]/div/div/form/div[1]/input")
        return element

    @property
    def element_password(self):
        element = self.driver.find_element_by_xpath(u"//body/div[3]/div/div[2]/div/div/form/div[2]/input")
        return element


    @property
    def element_submit(self):
        element = self.driver.find_element_by_id(u"comm-submit")
        return element


    @property
    def element_choose(self):
        element = self.driver.find_element_by_link_text(u"搜索")
        return element

    def go_to_search(self):
        time.sleep(5)
        self.element_choose.click()
        time.sleep(5)

    @property
    def element_search_input(self):
        element = self.driver.find_element_by_name(u"kw")
        return element

    @property
    def element_search_button(self):
        element = self.driver.find_element_by_xpath(u"//body/div[3]/div/div[2]/div/div/div[2]/form/div/div/button")
        return element

    @property
    def element_link_button(self):
        element = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")
        return element


