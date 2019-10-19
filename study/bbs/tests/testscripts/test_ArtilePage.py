# encoding:utf-8
import unittest
from selenium import webdriver
import time
from tests.ovc1024.ArtilePage import ArtilePage


class TestArtile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.locationpage = ArtilePage(self.driver)
        self.locationpage.open()

    def tearDown(self):
        self.driver.quit()

#1.登录
    def test_resigercase01(self):
        info = { u'email': u'487296792@qq.com', u'password': u'zhang1314520'}
        self.locationpage.register(info)
        time.sleep(4)

        exp=u"张军"
        serch=self.driver.find_element_by_xpath(u"//nav/div/div[4]/a")
        act=serch.text
        self.assertEqual(exp,act)

# 2.跳转到文章页面
    def test_jumpartilecase02(self):
        info = {u'email': u'487296792@qq.com', u'password': u'zhang1314520'}
        self.locationpage.register(info)
        time.sleep(4)
        article_link = self.driver.find_element_by_xpath(u"//div[1]/div/a[3]")
        article_link.click()

        exp = u"发布文章"
        serch = self.driver.find_element_by_xpath(u"//div[3]/nav/a")
        act = serch.text
        self.assertEqual(exp, act)

# 3.跳回到首页面
    def test_backindexcase03(self):
        info = {u'email': u'487296792@qq.com', u'password': u'zhang1314520'}
        self.locationpage.register(info)
        time.sleep(4)
        article_link = self.driver.find_element_by_xpath(u"//div[1]/div/a[3]")
        article_link.click()

        back_index = self.driver.find_element_by_xpath(u"//div[3]/nav/ol/li[1]/a")
        back_index.click()

        exp=u"ThinkSAAS文字广告1"
        serch=self.driver.find_element_by_xpath(u"//div[3]/div[2]/div/div/div[1]/a")
        act = serch.text
        self.assertEqual(exp, act)

#4.通过文章标题点击文章
    def test_articletitlecase04(self):
        info = {u'email': u'487296792@qq.com', u'password': u'zhang1314520'}
        self.locationpage.register(info)
        time.sleep(4)
        article_link = self.driver.find_element_by_xpath(u"//div[1]/div/a[3]")
        article_link.click()

        article_titlebt=self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[2]/div/div[1]/a")
        article_titlebt.click()
        time.sleep(2)

        exp = u"宽度468px广告位"
        serch = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[1]/div/div[2]/div")
        act = serch.text
        self.assertEqual(exp, act)

#5.点击上一篇文章名
    def test_lastarticlecase05(self):
        info = {u'email': u'487296792@qq.com', u'password': u'zhang1314520'}
        self.locationpage.register(info)
        time.sleep(4)
        article_link = self.driver.find_element_by_xpath(u"//div[1]/div/a[3]")
        article_link.click()

        article_titlebt=self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[2]/div/div[1]/a")
        article_titlebt.click()
        time.sleep(2)

        last_artile = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[1]/div/div[4]/a")
        last_artile.click()

        exp = u"346365"
        serch = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[1]/div/h1")
        act = serch.text
        self.assertEqual(exp, act)

#6.点击下一篇文章名
    def test_nextarticlecase06(self):
        info = {u'email': u'487296792@qq.com', u'password': u'zhang1314520'}
        self.locationpage.register(info)
        time.sleep(4)
        article_link = self.driver.find_element_by_xpath(u"//div[1]/div/a[3]")
        article_link.click()

        article_titlebt=self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[2]/div/div[1]/a")
        article_titlebt.click()
        time.sleep(2)

        next_artile = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[1]/div/div[5]/a")
        next_artile.click()

        exp = u"rd24d14"
        serch = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[1]/div/h1")
        act = serch.text
        self.assertEqual(exp, act)

#7.点击最新文章
    def test_latestarticleecase07(self):
        info = {u'email': u'487296792@qq.com', u'password': u'zhang1314520'}
        self.locationpage.register(info)
        time.sleep(4)
        article_link = self.driver.find_element_by_xpath(u"//div[1]/div/a[3]")
        article_link.click()

        article_titlebt=self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[2]/div/div[1]/a")
        article_titlebt.click()
        time.sleep(2)

        latest_article = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[3]/div[2]/div/ul/li[3]/a")
        latest_article.click()

        exp = u"346365"
        serch = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[1]/div/h1")
        act = serch.text
        self.assertEqual(exp, act)


#8.点击一周热门
    def test_populararticlecase08(self):
        info = {u'email': u'487296792@qq.com', u'password': u'zhang1314520'}
        self.locationpage.register(info)
        time.sleep(4)
        article_link = self.driver.find_element_by_xpath(u"//div[1]/div/a[3]")
        article_link.click()

        popular_article = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[2]/div[2]/div[2]/div/ul/li/a")
        popular_article.click()

        exp = u"rd24d14"
        serch = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[1]/div/h1")
        act = serch.text
        self.assertEqual(exp, act)

#9.通过点击全部，跳到显示所有文章的页面
    def test_alltarticleecase09(self):
        info = {u'email': u'487296792@qq.com', u'password': u'zhang1314520'}
        self.locationpage.register(info)
        time.sleep(4)
        article_link = self.driver.find_element_by_xpath(u"//div[1]/div/a[3]")
        article_link.click()

        article_titlebt = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[2]/div/div[1]/a")
        article_titlebt.click()
        time.sleep(2)

        all_articles = self.driver.find_element_by_xpath(u"//div[3]/div[1]/a")
        all_articles.click()

        exp = u"发布文章"
        serch = self.driver.find_element_by_xpath(u"//div[3]/nav/a")
        act = serch.text
        self.assertEqual(exp, act)

#10.通过点击查看全文来查看文章
    def test_searcharticleecase10(self):
        info = {u'email': u'487296792@qq.com', u'password': u'zhang1314520'}
        self.locationpage.register(info)
        time.sleep(4)
        article_link = self.driver.find_element_by_xpath(u"//div[1]/div/a[3]")
        article_link.click()

        search_article = self.driver.find_element_by_xpath(u"/html/body/div[3]/div[2]/div[1]/div[2]/div/div[3]/a")
        search_article.click()

        exp = u"宽度468px广告位"
        serch = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[1]/div/div[2]/div")
        act = serch.text
        self.assertEqual(exp, act)


#11..翻页
    def test_searcharticleecase11(self):
        info = {u'email': u'487296792@qq.com', u'password': u'zhang1314520'}
        self.locationpage.register(info)
        time.sleep(4)
        article_link = self.driver.find_element_by_xpath(u"//div[1]/div/a[3]")
        article_link.click()

        filp = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[11]/nav/ul/li[2]/a")
        filp.click()

        exp = u"2"
        serch = self.driver.find_element_by_xpath(u"//div[3]/div[2]/div[1]/div[4]/nav/ul/li[2]/a")
        act = serch.text
        self.assertEqual(exp, act)






if __name__ == '__main__':
    unittest.main()
