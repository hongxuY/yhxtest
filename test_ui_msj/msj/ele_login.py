# coding:utf-8
import time
from test_ui_msj import write_config


class ele_from_login():

    # 传入driver
    def __init__(self, driver):
        self.driver = driver

    def write(self, xpath):
        chishu = int(write_config.wait_max_time / write_config.wait_time)
        for i in range(chishu):
            try:
                element = self.driver.find_element_by_xpath(xpath)
                print("在第%s秒找到这个控件" % (i / 2))
                return element

            except:
                time.sleep(write_config.wait_time)
                if i == (chishu - 1):
                    print("无法获取该控件")
                    return None

    # 切换密码登录按钮
    @property
    def ele_longin_by_pasword(self):
        xpath = '//*[@id="tab-second"]'
        ele = self.write(xpath)
        # ele = self.driver.find_element_by_xpath('//*[@id="tab-second"]')
        return ele

    # 输入用户名
    @property
    def ele_user(self):
        ele = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/input')
        return ele

    # 输入密码
    @property
    def ele_password(self):
        ele = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/form/div[2]/div/div[1]/div[2]/input')
        return ele

    # 登录按钮
    @property
    def ele_button_login(self):
        ele = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/button')
        return ele

    # 登录成功后码上检页面显示的登录用户名
    @property
    def ele_after_login_username(self):
        ele = self.driver.find_element_by_xpath(
            '//div[@class="navbar_webtitlename"]')
        return ele

    # 登录成功后码上检页面的标题
    @property
    def ele_after_login_title(self):
        ele = self.driver.title
        return ele

    # 登录成功后码上检页面的url
    @property
    def ele_after_login_url(self):
        ele = self.driver.current_url
        return ele
