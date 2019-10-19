class ArtilePage():

    url="http://47.92.220.226:8000/bbs2/"

    def __init__(self,driver):
        self.driver=driver

    def open(self):
        self.driver.get(self.url)

    def register(self,info):
        register_bt = self.driver.find_element_by_xpath(u"//nav/div/div[3]/a[1]")
        register_bt.click()
        self.element_email_input.send_keys(info[u'email'])
        self.element_password_input.send_keys(info[u'password'])
        element_submit = self.driver.find_element_by_xpath(u'//*[@id="comm-submit"]')
        element_submit.click()

    @property
    def element_email_input(self):
        element= self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div/div/form/div[1]/input")
        return element

    @property
    def element_password_input(self):
        element = self.driver.find_element_by_xpath(u"//div[3]/div/div[2]/div/div/form/div[2]/input")
        return element


