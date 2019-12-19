# encoding:utf_8

class FirstPage():

    url = "http://47.92.220.226:8000/bbs2/"

    def __init__(self,driver):
        self.driver = driver
    def open(self):
        self.driver.get(self.url)

    def register(self,mem_register):
        self.ele_email_input.send_keys(mem_register["email"])
        self.ele_password_input.send_keys(mem_register["password"])
        self.ele_cpassword_input.send_keys(mem_register["cpassword"])
        self.ele_uname_input.send_keys(mem_register["username"])

    def login_in(self,user_benren):
        self.ele_email_input1.send_keys(user_benren["email"])
        self.ele_password_input1.send_keys(user_benren["password"])

    @property
    def ele_email_input(self):
        element = self.driver.find_element_by_name(u"email")
        return element

    @property
    def ele_password_input(self):
        element = self.driver.find_element_by_name(u"pwd")
        return element

    @property
    def ele_cpassword_input(self):
        element = self.driver.find_element_by_xpath(u"//body/div[3]/div/div[2]/div/div/form/div[3]/input")
        return element

    @property
    def ele_uname_input(self):
        element = self.driver.find_element_by_name(u"username")
        return element

    @property
    def ele_email_input1(self):
        element = self.driver.find_element_by_name(u"email")
        return element

    @property
    def ele_password_input1(self):
        element = self.driver.find_element_by_name(u"pwd")
        return element



