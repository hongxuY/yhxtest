# encoding:utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from laodao_config import url
# from laodao_opean_base import if_pageOpean_juage_base

class LaoDaoPage():

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def denglu(self, data):
        self.driver.find_element_by_xpath('//div[3]/a[1]').click()
        self.driver.find_element_by_xpath('//form/div[1]/input').send_keys(data['email'])
        self.driver.find_element_by_xpath('//form/div[2]/input').send_keys(data['password'])
        self.driver.find_element_by_id('comm-submit').click()

    # 登录成功之后等待
    def dengdai(self):
        try:
            WebDriverWait(self.driver, 3.5).until(
                expected_conditions.text_to_be_present_in_element((By.XPATH, '//nav/div/div[4]/a'), u'闫振兴'))
            # print ('登录跳转成功')
        except:
            print ("网速不好，重新测试")

    #     点击登录跳转到首页属性
    @property
    def find_shouye(self):
        self.driver.find_element_by_xpath('//nav/ol/li[1]/a').click()

    # 登录之手返回首页测试
    @property
    def test_return_shouye(self):
        return self.driver.current_url

    # 点回唠叨页面
    @property
    def return_laodao(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div/a[5]').click()

    # 发送唠叨
    @property
    def send_laodao(self):
        self.driver.find_element_by_id('content').send_keys(u'唠叨测试')
        self.driver.find_element_by_xpath('//form/div/div/button').click()

    # 发送成功之后等待
    @property
    def wait(self):
        try:
            WebDriverWait(self.driver, 3.5).until(
                expected_conditions.text_to_be_present_in_element((By.XPATH, '//div[2]/div[1]/a'), u'闫振兴'))
        except:
            print ("网络卡顿。")
    # 测试唠叨有没有发布成功
    @property
    def test_laodao(self):
        return self.driver.find_element_by_xpath('//div[2]/div/ul/li[1]/a').text

    # 点击用户头像
    @property
    def click_imge(self):
        self.driver.find_element_by_xpath('//div[3]/ul/li[1]/a/img').click()

    # 点击头像成功的测试
    @property
    def test_click_imge(self):
        return self.driver.find_element_by_xpath('//div/div[2]/a[5]').text

    # 回复消息
    @property
    def huifu_massage(self):
        self.driver.find_element_by_xpath('//div[3]/ul/li[2]/p/a').click()
        self.driver.find_element_by_xpath('//div[2]/form/textarea').send_keys(u'UI自动化回复测试成功')
        self.driver.find_element_by_xpath('//div[2]/form/div/button').click()

    # 回复消息成功测试
    @property
    def test_huifu(self):
        return self.driver.find_element_by_xpath('//div[1]/ul/li/div[2]/p[2]').text

    # 跳转页面：
    def tiaozhuanPage(self):
        self.driver.find_element_by_xpath('//div[5]/nav/ul/li[2]/a').click()

    # 测试页面跳转成功
    @property
    def test_tiaozhuan(self):
        return self.driver.current_url

    # 评价消息
    @property
    def pingjia(self):
        self.driver.find_element_by_xpath('//ul/li[1]/span[2]/span[3]/a').click()
        self.driver.find_element_by_xpath('//div[2]/form/textarea').send_keys(u'UI测试评价成功')
        self.driver.find_element_by_xpath('//div[2]/form/div/button').click()

    # 点击用户名
    def click_name(self):
        self.driver.find_element_by_xpath('//ul/li[2]/div[1]/a').click()


