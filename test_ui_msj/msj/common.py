#coding:utf-8
from test_ui_msj.msj.ele_login import ele_from_login
import time

class Common():

    #登录方法
    #传入参数：driver，登录账号，密码
    #返回参数：msg字典
    #           username：登录用户的用户名
    #           title：登录成功后页面的标题
    #           url:登录成功后页面的URL
    def login(self,driver,user,password):
        self.ele_login=ele_from_login(driver)
        self.ele_login.ele_longin_by_pasword.click()
        self.ele_login.ele_user.send_keys(user)
        self.ele_login.ele_password.send_keys(password)
        self.ele_login.ele_button_login.click()

        time.sleep(2)

        msg={}

        username=self.ele_login.ele_after_login_username.text
        title=self.ele_login.ele_after_login_title
        url=self.ele_login.ele_after_login_url

        msg["username"]=username
        msg["title"] = title
        msg["url"] = url

        return msg

