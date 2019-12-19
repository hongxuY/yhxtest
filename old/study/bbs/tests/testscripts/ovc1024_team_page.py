#encoding:utf-8


class TeamPage():

    url_ovc1024 = "http://47.92.220.226:8000/bbs2/index.php"

    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url_ovc1024)

    def register(self,register_data):
        self.ovc_account.send_keys(register_data['account'])
        self.ovc_password.send_keys(register_data['password'])

    @property
    def ovc_register(self):
        element = self.driver.find_element_by_xpath(u"//div/div[3]/a[1]")
        return element

    @property
    def ovc_account(self):
        element = self.driver.find_element_by_xpath(u"//div[1]/input")
        return element

    @property
    def ovc_password(self):
        element = self.driver.find_element_by_name(u"pwd")
        return element

    @property
    def ovc_login(self):
        element = self.driver.find_element_by_id(u"comm-submit")
        return element

    @property
    def ovc_team(self):
        element = self.driver.find_element_by_xpath(u"//div[1]/div/a[2]")
        return element

    @property
    def ovc_team_info01(self):
        element = self.driver.find_element_by_xpath(u"//div/div/div[2]/div[2]/div/div[2]/a")
        return element

    @property
    def ovc_team_info02(self):
        element = self.driver.find_element_by_xpath(u"//div[2]/div[2]/div/div[2]/a")
        return element








