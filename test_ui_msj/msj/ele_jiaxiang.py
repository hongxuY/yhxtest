# coding:utf-8

class ele_from_jiaxiang():

    # 传入driver
    def __init__(self, driver):
        self.driver = driver

    # 新增加项包按钮
    @property
    def ele_(self):
        ele = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/section/div/div[1]/div[2]/button[1]')
        return ele

