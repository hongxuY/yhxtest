# coding:utf-8
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class TongCheng():
    # 网页地址
    url = "http://47.92.220.226:8000/bbs2/index.php"

    # 传入driver
    def __init__(self, driver):
        self.driver = driver

    # 打开网页
    def open(self):
        self.driver.get(self.url)

    # 登录方法
    def login(self, user):
        self.ele_longin.click()
        self.ele_username.send_keys(user["username"])
        self.ele_password.send_keys(user["password"])
        self.ele_submit.click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, '//div[@class="card-header"]'), u"最新签到用户"))


    # 跳转到同城的方法
    def go_to_tongcheng(self):
        self.ele_choose.click()
        time.sleep(4)

    # 首页登录按钮
    @property
    def ele_longin(self):
        ele = self.driver.find_element_by_xpath(u'//div[@class="ts-user-nav"]/a[1]')
        return ele

    # 邮箱输入框
    @property
    def ele_username(self):
        ele = self.driver.find_element_by_xpath(u'/html/body/div[3]/div/div[2]/div/div/form/div[1]/input')
        return ele

    # 密码输入框
    @property
    def ele_password(self):
        ele = self.driver.find_element_by_xpath(u"/html/body/div[3]/div/div[2]/div/div/form/div[2]/input")
        return ele

    # 提交登录按钮
    @property
    def ele_submit(self):
        ele = self.driver.find_element_by_id(u"comm-submit")
        return ele

    # 同城模块的接口按钮
    @property
    def ele_choose(self):
        ele = self.driver.find_element_by_link_text(u"同城")
        return ele

    # 选择同城里的加入武汉按钮
    @property
    def ele_wuhan(self):
        ele = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/ul/li[1]/div[2]/div[3]/a")
        return ele

    # 北京同城里面的北京图标元素
    @property
    def ele_wuhan_img(self):
        ele = self.driver.find_element_by_xpath('//div[@class="photo"]/img')
        return ele

    # 选择同城里的加入北京按钮
    @property
    def ele_beijing(self):
        ele = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[2]/div/ul/li[2]/div[2]/div[3]/a")
        return ele

    # 北京同城里面的北京图标元素
    @property
    def ele_beijing_img(self):
        ele = self.driver.find_element_by_xpath('//div[@class="photo"]/img')
        return ele

    # 退出同城按钮
    @property
    def ele_exit_tongcheng(self):
        ele = self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[2]/h1/a")
        return ele

    # 选择加入同城的提示
    @property
    def ele_card_header(self):
        ele = self.driver.find_element_by_class_name("card-header")
        return ele

    # 同城用户里第一个用户的头像
    @property
    def ele_touxiang(self):
        ele = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]/div/ul/li/a/img")
        return ele

    # 用户个人页面里的用户头像
    @property
    def ele_touxiang_souye(self):
        ele = self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[1]/div[1]/div/img")
        return ele

    # 同城用户里第一个用户的用户名
    @property
    def ele_name(self):
        ele = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]/div/ul/li/div/a")
        return ele

    # 同城图片里的第一张图片
    @property
    def ele_photo(self):
        ele = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/ul/li/a/img")
        return ele

    # 同城图片里第一张图片跳转后页面的图片
    @property
    def ele_photo1(self):
        ele = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div[2]/img")
        return ele

    # 同城贴子里发帖人头像
    @property
    def ele_t_phtot(self):
        ele = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[3]/div[2]/div/ul/li/div[1]/a/img")
        return ele

    # 同城帖子里发帖人用户名
    @property
    def ele_t_name(self):
        ele = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/div[3]/div[2]/div/ul/li/div[2]/div[2]/span[2]/a[1]")
        return ele

    # 同城帖子里帖子标题
    @property
    def ele_t_title(self):
        ele = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/div[3]/div[2]/div/ul/li/div[2]/div[1]/a")
        return ele

    # 同城帖子里发帖人所在小组名称
    @property
    def ele_t_class(self):
        ele = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/div[3]/div[2]/div/ul/li/div[2]/div[2]/span[1]/a")
        return ele

    # 同城帖子里帖子回复数
    @property
    def ele_t_huifu(self):
        ele = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div[1]/div[3]/div[2]/div/ul/li/div[2]/div[2]/span[2]/a[2]")
        return ele

    # 点击同城帖子里帖子标题跳转到帖子页面的帖子标题
    @property
    def ele_t_title1(self):
        ele = self.driver.find_element_by_xpath('//div[@class="card-body"]/h1')
        return ele

    # 发帖人所在小组首页的小组名
    @property
    def ele_t_class1(self):
        ele = self.driver.find_element_by_xpath('//div[@class="media-body"]/h1')
        return ele

    # 唠唠叨叨里第一个唠叨的发送者头像
    @property
    def ele_l_photo(self):
        ele = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div/ul/li/span[1]/a/img')
        return ele

    # 唠唠叨叨里第一个唠叨的发送者用户名
    @property
    def ele_l_name(self):
        ele = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div/ul/li/span[2]/span[1]/a')
        return ele

    # 唠唠叨叨里第一个唠叨的评价
    @property
    def ele_l_ping(self):
        ele = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div/ul/li/span[2]/span[3]/a')
        return ele

    # 唠唠叨叨里第一个唠叨的内容
    @property
    def ele_l_laodao(self):
        ele = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div/ul/li/span[2]/span[2]/p')
        return ele

    # 唠唠叨叨里第一个唠叨的内容对应的唠叨页面正文内容
    @property
    def ele_l_laodao1(self):
        ele = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/ul/li[2]/div[2]/p')
        return ele

    # 同城文章里第一篇文章
    @property
    def ele_wenzhang(self):
        ele = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div/ul/li/a')
        return ele

    # 同城文章里第一篇文章对应跳转的文章页面的标题
    @property
    def ele_wenzhang1(self):
        ele = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/h1')
        return ele

    # 获取全部同城的链接
    @property
    def ele_all(self):
        ele = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[3]/div/a')
        return ele

    # 全部同城页面的提示
    @property
    def ele_al(self):
        ele = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]')
        return ele
