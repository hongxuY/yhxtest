# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

# 启动火狐浏览器
driver = webdriver.Firefox()

# 打开url
driver.get("http://www.baidu.com")

# ========================================================================================
# 获取控件（全部都可以分为单复数）


# 通过ID选择器获取控件
ele = driver.find_element_by_id('kw')
ele = driver.find_element(By.ID, 'kw')

# 通过name获取控件
ele = driver.find_element_by_name('wd')

# 通过xpath获取控件
ele = driver.find_element_by_xpath('//input[@class="s_ipt"]')
ele = driver.find_element_by_xpath('//*[@id="kw"]')

# 通过class选择器获取控件
ele = driver.find_element_by_class_name('s_ipt')

# 通过链接文字获取控件
ele = driver.find_element_by_link_text('新闻')

# 通过部分链接文字获取控件
ele = driver.find_element_by_partial_link_text('新')

# 通过css路径获取控件
# ele = driver.find_element_by_css_selector()

# 通过标签名获取控件
ele = driver.find_elements_by_tag_name('input')

# ===================================================================================

# 返回上一步
driver.back()

# 前进一步
driver.forward()

# 截屏
driver.get_screenshot_as_file(r"d:\\aa.png")

# 退出
driver.quit()
