# coding:utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class register_page():
    url = "http://47.92.220.226:8000/bbs2/index.php?app=user&ac=login"
    title = u"登录_用户_OVC1024"
    keyword_xpath = u'//div[@class="fs24"]'
    keyword_text = u"用户登录"

    def __init__(self, driver):
        self.driver = driver

    def if_page_open_success(self):
        act_page_title = self.driver.title
        print "[debug] act_page_title:%s" % act_page_title
        act_page_url = self.driver.current_url
        print "[debug] act_page_url:%s" % act_page_url
        act_page_keyword_ele = self.ele_page_keyword
        print "[debug] act_page_keyword_ele:%s" % act_page_keyword_ele
        WebDriverWait(self.driver,10).until(expected_conditions.text_to_be_present_in_element((By.XPATH,self.keyword_xpath),self.keyword_text))


        faile_dict = {}

        if self.title != act_page_title:
            faile_dict["title"] = {"exp_value": self.title, "act_value": act_page_title}
        if self.url != act_page_url:
            faile_dict["url"] = {"exp_value": self.url, "act_value": act_page_url}
        if self.keyword_text != act_page_keyword_ele.text:
            faile_dict["key_word"] = {"exp_value": self.keyword_text, "act_value": act_page_keyword_ele.text}

        if len(faile_dict) == 0:
            return True, {}
        else:
            return False, faile_dict

    @property
    def ele_page_keyword(self):
        ele = self.driver.find_element_by_xpath(self.keyword_xpath)
        return ele
