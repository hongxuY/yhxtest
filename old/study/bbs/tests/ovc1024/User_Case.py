#  coding:utf-8

class UserPage():

    url='http://47.92.220.226:8000/bbs2/'

    def __init__(self,driver):
        self.driver=driver

    def open(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    @property
    def ele_register_user(self):
        element = self.driver.find_element_by_xpath(u"/html/body/nav/div/div[3]/a[2]")
        return element

    @property
    def ele_input_username(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div/div[2]/div/div/form/div[4]/input')
        return element

    @property
    def ele_input_email(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div/div[2]/div/div/form/div[1]/input')
        return element

    @property
    def ele_input_password(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div/div[2]/div/div/form/div[2]/input')
        return element

    @property
    def ele_input_password_enter(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div/div[2]/div/div/form/div[3]/input')
        return element

    @property
    def ele_register(self):
        element = self.driver.find_element_by_id(u"comm-submit")
        return element

    @property
    def chioce_user(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[1]/div/a[6]')
        return element

    @property
    def chioce_user_name(self):
        element = self.driver.find_element_by_xpath(u'//div[1]/dl/dd/ul/li[1]/p/a')
        return element

    @property
    def user_score(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div[2]/div[1]/div/div/dl/dd[6]')
        return element

    @property
    def chioce_user_photo(self):
        element = self.driver.find_element_by_xpath(u'//div[1]/dl/dd/ul/li[1]/div/a/img')
        return element

    @property
    def user_UID(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div[2]/div[1]/div/div/dl/dd[1]')
        return element

    @property
    def user_Sex(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div[2]/div[1]/div/div/dl/dd[2]')
        return element

    @property
    def user_introdoction(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div[2]/div[1]/div/div/dl/dd[3]')
        return element

    @property
    def user_fans(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div[1]/div/div[2]/a[5]')
        return element

    @property
    def user_guanzhu(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div[1]/div/div[2]/a[5]')
        return element

    @property
    def send_text(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div[1]/div/div[1]/div[2]/div/a[2]')
        return element

    @property
    def text(self):
        element = self.driver.find_element_by_xpath(u'/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/div/textarea')
        return element

    @property
    def enter_send(self):
        element=self.driver.find_element_by_xpath(u'/html/body/div[3]/div/div[2]/div/div[2]/form/div[3]/div/button')
        return element



