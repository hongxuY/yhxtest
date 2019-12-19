#  coding:utf-8


import unittest
from selenium import webdriver
from tests.ovc1024.User_Case import UserPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.User_Case=UserPage(self.driver)
        self.User_Case.open()

    def Quit(self):
        self.User_Case.quit()

    # 注册
    def test_register_user(self):
        register_data = {
            'user_name': u'W_ang_95',
            'user_email': u'W_ang@qq.com',
            'user_password': u'123',
            'user_password_enter': u'123',
        }
        self.User_Case.ele_register_user.click()

        self.User_Case.ele_input_username.send_keys(register_data['user_name'])
        self.User_Case.ele_input_email.send_keys(register_data['user_email'])
        self.User_Case.ele_input_password.send_keys(register_data['user_password'])
        self.User_Case.ele_input_password_enter.send_keys(register_data['user_password_enter'])

        self.User_Case.ele_register.click()

        act=self.driver.current_url
        exp=u'http://47.92.220.226:8000/bbs2/'

        self.assertEqual(act, exp)

    # 登录成功之后等待
    def dengdai(self):
        WebDriverWait(self.driver, 3.5).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, '/html/body/nav/div/div[4]/a'), u'W_ang_95'))

    #首页点击用户，在用户积分榜点击用户用户名查看用户对应积分
    def test_user_name(self):
        self.User_Case.chioce_user.click()
        self.User_Case.chioce_user_name.click()

        act = self.User_Case.user_score.text
        exp = u'30'
        self.assertEqual(act, exp)

    #首页点击用户,点击头像查看用户对应积分
    def test_user_photo(self):
        self.User_Case.chioce_user.click()
        self.User_Case.chioce_user_photo.click()

        act = self.User_Case.user_score.text
        exp=u'30'
        self.assertEqual(act, exp)

    # 首页点击用户，点击用户用户名，可查看用户id
    def test_user_UID(self):
        self.User_Case.chioce_user.click()
        self.User_Case.chioce_user_name.click()

        act=self.User_Case.user_UID.text
        exp=u'3'
        self.assertEqual(act, exp)

    #  首页点击用户，点击用户用户名，可查看用户性别
    def test_user_sex(self):
        self.User_Case.chioce_user.click()
        self.User_Case.chioce_user_name.click()

        act = self.User_Case.user_Sex.text
        exp = u'女'
        self.assertEqual(act, exp)

    # 首页点击用户,点击用户头像，可查看用户自我介绍
    def test_user_introdoction(self):
        self.User_Case.chioce_user.click()
        self.User_Case.chioce_user_photo.click()

        act = self.User_Case.user_introdoction.text
        exp = u'还没有介绍'
        self.assertEqual(act, exp)

    # 首页点击用户,点击用户头像，点击粉丝可查看用户粉丝数
    def test_user_fans(self):
        self.User_Case.chioce_user.click()
        self.User_Case.chioce_user_photo.click()
        self.User_Case.user_fans.click()

        fans_name=self.driver.find_element_by_xpath(u'/html/body/div[3]/div[2]/div[1]/div/div/div[1]/dl/dd').text
        act = fans_name
        exp = u'闫振兴'
        self.assertEqual(act,exp)

    # 首页点击用户,点击用户用户名，点击关注可关注此用户
    def test_guanzhu(self):
        self.User_Case.chioce_user.click()
        self.User_Case.chioce_user_name.click()
        self.User_Case.user_guanzhu.click()

        act=self.driver.find_element_by_xpath(u'/html/body/div[3]/div[1]/div/div[1]/div[2]/div/a[1]').text
        exp=u'取消关注'
        self.assertEqual(act, exp)

    # 首页点击用户,点击用户用户名，点击发消息可向此用户发消息
    def test_send_text(self):
        self.User_Case.send_text.click()
        self.User_Case.text.send_keys(u'用户测试')
        self.User_Case.enter_send.click()

        act=self.driver.current_url
        exp=u'http://47.92.220.226:8000/bbs2/index.php?app=message&ac=my'
        self.assertEqual(act, exp)







if __name__ == '__main__':
    unittest.main()
