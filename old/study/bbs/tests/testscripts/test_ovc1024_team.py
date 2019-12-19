# encoding:utf-8
import unittest
from selenium import webdriver
from tests.testscripts.ovc1024_team_page import TeamPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Firefox()
        self.team_page = TeamPage(self.driver)
        self.team_page.open()
    def tearDown(self):
        self.driver.quit()


    def test_register_case01(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()

    def test_team_case02(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u"//div[1]/div/a[2]"),u"小组"))
        self.team_page.ovc_team.click()

    def test_home_case03(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u"//div[1]/div/a[2]"),u"小组"))
        self.team_page.ovc_team.click()
        home_page = self.driver.find_element_by_xpath(u"//ol/li[1]/a")
        home_page.click()

    def test_creat_team_case04(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()
        WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.XPATH, u"//div[1]/div/a[2]"), u"小组"))
        self.team_page.ovc_team.click()
        creat_team = self.driver.find_element_by_link_text(u"创建小组")
        creat_team.click()
        team_name = self.driver.find_element_by_name(u"groupname")
        team_name.send_keys(u"我们的目标是永不脱发")
        team_introduce = self.driver.find_element_by_name(u"groupdesc")
        team_introduce.send_keys(u"记得那天在夕阳下的奔跑，那是我逝去的青春！")
        team_tag = self.driver.find_element_by_name(u"tag")
        team_tag.send_keys(u"没有bug就没有伤害！")
        creat_team_bt = self.driver.find_element_by_xpath(u"//div[2]/form/button")
        creat_team_bt.click()

    def test_team_page_case05(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u"//div[1]/div/a[2]"),u"小组"))
        self.team_page.ovc_team.click()
        page_bt = self.driver.find_element_by_xpath(u"//div[3]/div/div[1]/div/div")
        page_bt.click()

    def test_team_info_case0601(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u"//div[1]/div/a[2]"),u"小组"))
        self.team_page.ovc_team.click()
        self.team_page.ovc_team_info01.click()

    def test_team_info_case0602(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u"//div[1]/div/a[2]"),u"小组"))
        self.team_page.ovc_team.click()
        self.team_page.ovc_team_info02.click()

    def test_team_entry_caose07(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u"//div[1]/div/a[2]"),u"小组"))
        self.team_page.ovc_team.click()
        team_info2 = self.driver.find_element_by_xpath(u"//div[2]/div[2]/div/div[2]/a")
        team_info2.click()
        join_or_quit_team = self.driver.find_element_by_xpath(u"//div[1]/div/div[2]/div/span/a")
        join_or_quit_team.click()

    def test_team_issuance_case08(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u"//div[1]/div/a[2]"),u"小组"))
        self.team_page.ovc_team.click()
        self.team_page.ovc_team_info02.click()
        issuance = self.driver.find_element_by_link_text(u"发布帖子")
        issuance.click()

    def test_team_hot_note_case09(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u"//div[1]/div/a[2]"),u"小组"))
        self.team_page.ovc_team.click()
        hot_note = self.driver.find_element_by_xpath(u"//li[4]/div[1]/a")
        hot_note.click()

    def test_team_hot_note_team_case10(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u"//div[1]/div/a[2]"),u"小组"))
        self.team_page.ovc_team.click()
        hot_note_team = self.driver.find_element_by_xpath(u"//li[4]/div[2]/div[1]/a")
        hot_note_team.click()

    def test_team_recently_case11(self):
        register_data = {
            'account': u"1041135120@qq.com",
            'password': u'123456',
        }
        self.team_page.ovc_register.click()
        self.team_page.register(register_data)
        self.team_page.ovc_login.click()
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH,u"//div[1]/div/a[2]"),u"小组"))
        self.team_page.ovc_team.click()
        recently_team = self.driver.find_element_by_xpath(u"//div[2]/div/ul/li[1]/a")
        recently_team.click()

if __name__ == '__main__':
    unittest.main()
