#coding:utf-8
from test_ui_msj.msj.ele_login import ele_from_login

class Common():

    #登录方法
    #传入参数：driver，登录账号，密码

    def login(self,driver,user,password):
        self.ele_login=ele_from_login(driver)
        self.ele_login.ele_longin_by_pasword.click()
        self.ele_login.ele_user.send_keys(user)
        self.ele_login.ele_password.send_keys(password)
        self.ele_login.ele_button_login.click()




