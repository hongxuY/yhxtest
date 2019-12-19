# encoding:utf-8

class LocationPage():
    url = "http://47.92.220.226:8000/bbs2/index.php?app=user&ac=login"

    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def register(self,register_data):
        self.ele_email_input.send_keys(register_data['email'])
        self.ele_password_input.send_keys(register_data['password'])
        self.ele_lodin_bt.click()

    @property
    def ele_email_input(self):
        ele = self.driver.find_element_by_xpath(u'//div/form/div[1]/input')
        return ele
    @property
    def ele_password_input(self):
        ele = self.driver.find_element_by_xpath(u'//div/form/div[2]/input')
        return ele
    @property
    def ele_lodin_bt(self):
        ele = self.driver.find_element_by_id(u'comm-submit')
        return ele

    @property
    def ele_aptest(self):
        ele = self.driver.find_element_by_link_text(u'我的社区')
        return ele

    @property
    def ele_myphototest(self):
        ele = self.driver.find_element_by_xpath(u"//div[2]/ul[1]/li[5]/a")
        return ele

    @property
    def ele_mycitytest(self):
        ele = self.driver.find_element_by_xpath(u"//div[2]/ul[1]/li[6]/a")
        return ele

    @property
    def ele_basictest(self):
        ele = self.driver.find_element_by_link_text(u"基本信息")
        return ele

    @property
    def ele_installtest(self):
        ele = self.driver.find_element_by_xpath(u"//div[2]/ul[3]/li/a")
        return ele

    @property
    def instert_username(self):
        ele = self.driver.find_element_by_xpath(u"//form/div[1]/input")
        return ele

    @property
    def instert_sign(self):
        ele = self.driver.find_element_by_xpath(u"//form/div[3]/input")
        return ele

    @property
    def instert_introduce(self):
        ele = self.driver.find_element_by_xpath(u"//form/div[4]/textarea")
        return ele

    @property
    def instert_install(self):
        ele = self.driver.find_element_by_xpath(u"//form/button")
        return ele

    @property
    def instert_return(self):
        ele = self.driver.find_element_by_xpath(u"//p[2]/a")
        return ele

    @property
    def ele_password(self):
        ele = self.driver.find_element_by_link_text(u"修改密码")
        return ele

    @property
    def instert_password(self):
        ele = self.driver.find_element_by_xpath(u"//form/div[1]/input")
        return ele

    @property
    def instert_newpassword(self):
        ele = self.driver.find_element_by_xpath(u"//form/div[2]/input")
        return ele

    @property
    def instert_rwpassword(self):
        ele = self.driver.find_element_by_xpath(u"//form/div[3]/input")
        return ele

    @property
    def instert_inspassword(self):
        ele = self.driver.find_element_by_xpath(u"//form/button")
        return ele

    @property
    def instert_return3(self):
        ele = self.driver.find_element_by_xpath(u"//p[2]/a")
        return ele

    @property
    def ele_account_test(self):
        ele = self.driver.find_element_by_xpath(u"//div/div/div[1]/a[4]")
        return ele

    @property
    def instert_newemail(self):
        ele = self.driver.find_element_by_xpath(u"//form/div[2]/input")
        return ele

    @property
    def instert_insemail(self):
        ele = self.driver.find_element_by_xpath(u"//form/button")
        return ele

    @property
    def instert_return4(self):
        ele = self.driver.find_element_by_xpath(u"//p[2]/a")
        return ele

    @property
    def ele_label(self):
        ele = self.driver.find_element_by_link_text(u"个人标签")
        return ele

    @property
    def instert_inslabel(self):
        ele = self.driver.find_element_by_id(u"tags")
        return ele

    @property
    def instert_add(self):
        ele = self.driver.find_element_by_xpath(u"//div[2]/button")
        return ele

