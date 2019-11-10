#coding:utf-8

from selenium import webdriver
from test_ui_msj import config
from test_ui_msj.msj.ele_login import ele_from_login
import time



driver = webdriver.Firefox()
url=config.URL
driver.get(url)
driver.maximize_window()

time.sleep(2)

ele_login=ele_from_login(driver)

ele=ele_login.ele_longin_by_pasword
ele.click()


ele_user=ele_login.ele_user
user=config.USER
ele_user.send_keys(user)

ele_password=ele_login.ele_password
password=config.PASSWORD
ele_password.send_keys(password)

ele_login=ele_login.ele_button_login
ele_login.click()

