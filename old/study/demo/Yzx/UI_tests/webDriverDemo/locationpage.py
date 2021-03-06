#encoding:utf-8

class LocationPage():
    url="http://47.92.220.226:8000//webdriver/location.html"

    def __init__(self,driver):
        self.driver=driver

    def open(self):
        self.driver.get(self.url)

    # 注册功能实现
    def regesit(self,regesit_data):
        self.element_username_input.send_keys(regesit_data['username'])
        self.element_email_input.send_keys(regesit_data['email'])
        self.element_password_input.send_keys(regesit_data['password'])
        self.element_confirm_password_input.send_keys(regesit_data['cpassword'])
        self.element_register.click()

    @property
    def element_username_input(self):
        element=self.driver.find_element_by_id(u'username1')
        return element

    @property
    def element_email_input(self):
        element = self.driver.find_element_by_name(u'email')
        return element

    @property
    def element_password_input(self):
        element = self.driver.find_element_by_id(u'password')
        return element

    @property
    def element_confirm_password_input(self):
        element = self.driver.find_element_by_css_selector(u'#confirm_password')
        return element

    @property
    def element_register(self):
        element = self.driver.find_element_by_xpath(u"//td[@colspan='2']/input[1]")
        return element

    @property
    def return_msg(self):
        element=self.driver.find_element_by_id(u'regmsg')
        return element