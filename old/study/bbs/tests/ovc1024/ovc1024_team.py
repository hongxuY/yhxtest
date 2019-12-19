#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

url_ovc1024 = "http://47.92.220.226:8000/bbs2/index.php"
driver.get(url_ovc1024)

#登录
register = driver.find_element_by_xpath(u"//div/div[3]/a[1]")
register.click()
account = driver.find_element_by_xpath(u"//div[1]/input")
account.send_keys(u"1041135120@qq.com")
password = driver.find_element_by_name(u"pwd")
password.send_keys(u"123456")
login = driver.find_element_by_id(u"comm-submit")
login.click()
WebDriverWait(driver, 20).until(expected_conditions.text_to_be_present_in_element((By.XPATH, u"//div[1]/div/a[2]"), u'小组'))
#进入小组
team = driver.find_element_by_xpath(u"//div[1]/div/a[2]")
team.click()

# 返回首页功能
# home_page = driver.find_element_by_xpath(u"//ol/li[1]/a")
# home_page.click()

#创建小组功能
# creat_team = driver.find_element_by_link_text(u"创建小组")
# creat_team.click()
#
# team_name = driver.find_element_by_name(u"groupname")
# team_name.send_keys(u"我们的目标是永不脱发")
#
# team_introduce = driver.find_element_by_name(u"groupdesc")
# team_introduce.send_keys(u"记得那天在夕阳下的奔跑，那是我逝去的青春！")
#
# team_tag = driver.find_element_by_name(u"tag")
# team_tag.send_keys(u"没有bug就没有伤害！")
#
# creat_team_bt = driver.find_element_by_xpath(u"//div[2]/form/button")
# creat_team_bt.click()

#切换小组页面
# page_bt = driver.find_element_by_xpath(u"//div[3]/div/div[1]/div/div")
# page_bt.click()

#查看小组信息
team_info = driver.find_element_by_css_selector(u"div.col-md-6:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)")
team_info.click()
team_info2 = driver.find_element_by_xpath(u"//div[2]/div[2]/div/div[2]/a")
team_info2.click()

#加入小组&退出小组
# join_team = driver.find_element_by_xpath(u"//div[1]/div/div[2]/div/span/a")
# join_team.click()
# time.sleep(6)
# quit_team = driver.find_element_by_xpath(u"//div[1]/div/div[2]/div/span/a")
# quit_team.click()

#发布帖子
# issuance = driver.find_element_by_link_text(u"发布帖子")
# issuance.click()

#输入标题
# title = driver.find_element_by_xpath(u"//form/div[1]/input")
# title.send_keys(u"我变秃了，也变强了！")
#
# bform = driver.find_element_by_xpath(u"/html/body/nav")
# bform.click()
# switch0 = driver.switch_to.f()
# form = driver.find_element_by_xpath(u"/html/body/div[3]/div")
# form.click()
# iform = driver.find_element_by_xpath(u"/html/body/div[3]/div/div/div")
# iform.click()
# mform = driver.find_element_by_xpath(u"/html/body/div[3]/div/div/div/div[2]/form")
# mform.click()

#获取小组成员
# team_member = driver.find_element_by_css_selector(u"a.text-black-50")
# team_member.click()

#查看帖子
team_note = driver.find_element_by_xpath(u"//li/div[2]/div[1]/a")
team_note.click()

#编辑帖子
# team_note_modify = driver.find_element_by_xpath(u"//div[3]/div[3]/a[1]")
# team_note_modify.click()

#删除帖子
# team_note_delete = driver.find_element_by_xpath(u"//div[3]/div[3]/a[2]")
# team_note_delete.click()

#热门帖子
# hot_note = driver.find_element_by_xpath(u"//li[4]/div[1]/a")
# hot_note.click()

#热门帖子所在小组
# hot_note_team = driver.find_element_by_xpath(u"//li[4]/div[2]/div[1]/a")
# hot_note_team.click()
#
# #最新创建的小组
# recently_team = driver.find_element_by_xpath(u"//div[2]/div/ul/li[1]/a")
# recently_team.click()