# -*- coding: UTF-8 -*-

from locust import HttpLocust, TaskSet, task, events
from util import *
import Queue
import logging
import datetime
import os
import collections
from gevent._semaphore import Semaphore
# all_locusts_spawned = Semaphore()
# all_locusts_spawned.acquire()
#
#
# def on_hatch_complete(**kw):
#     all_locusts_spawned.release()
#
# events.hatch_complete += on_hatch_complete


class YJKTask(TaskSet):
    _headers = {"Content-Type": "application/json; charset=UTF-8"}
    # _informationId = 411068  # 测试环境
    _informationId = 214894  # 生产环境
    # _goodsId = "527785cc-5030-44eb-92fc-b304b99ac7ff"  # 测试环境
    _goodsId = "8c125817-b7bb-47d1-a474-cfb90f13e73d"  # 生产环境

    # 并发用户初始化
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()
        #all_locusts_spawned.wait()

    # 提交接口请求，返回代码为200时返回接口响应数据，否则记录错误日志并触发failure事件给locust
    def post(self, url, json, notlogin=True):
        if notlogin:
            if self._token:
                json["token"]=self._token
            else:
                return None

        json = updateRequest(json)
        with self.client.post(url, json=json, headers=self._headers, catch_response=True) as post_resp:
            if post_resp.status_code == 200:
                if len(post_resp.content) > 0:
                    resp = post_resp.json()
                    if resp['code'] == 200:
                        post_resp.success()
                        return resp
                    else:
                        post_resp.failure('YJK Response Code:%d!' % resp['code'])
                        self.locust.logger.error("API: %s%s, Request: %s; YJK Response Code: %s, Msg: %s" % (self.locust.host, url, json, resp['code'], resp['msg']))
                        return None

            post_resp.failure('Request failure!HTTP Response Status Code: %s, HTTP Response content: %s!' % (post_resp.status_code, post_resp.content))
            self.locust.logger.error('API: %s%s, Request: %s; HTTP Response Status Code: %s, HTTP Response content: %s!' % (self.locust.host, url, json, post_resp.status_code, post_resp.content))
        return None

    @task(0)
    def get(self):
        with self.client.get('status.html', catch_response=True) as post_resp:
            if post_resp.status_code != 200:
                post_resp.failure('Request failure!HTTP Response Status Code: %s, HTTP Response content: %s!' % (post_resp.status_code, post_resp.content))
                self.locust.logger.error('status.html Request failure!HTTP Response Status Code: %s, HTTP Response content: %s!' % (post_resp.status_code, post_resp.content))

    # 用户登录，从用户队列中取手机号，不重复使用
    def login(self):
        try:
            self._phonenum = self.locust.user_queue.get(timeout=10)
        except Queue.Empty:
            self.locust.logger.error('Account queue data run out, test ended.')
            exit(0)
        self._token = ''
        self._userid = ''
        dict={"identifyingCode": "121", "phoneNumber": self._phonenum}
        url = "10001/login2"
        resp = self.post(url, dict, False)
        if resp!=None:
            self._token = resp["data"]["token"]
            self._userid = resp["data"]["userId"]
            self.locust.logger.info('User login OK, phone number:%s, token:%s' % (self._phonenum, self._token))

    # 获取用户卡片信息
    @task(0)
    def getUserCardInfo(self):
        url = "hm/getUserCardInfo"
        dict = {}
        resp = self.post(url, dict)

    # 获取用户步行信息
    @task(0)
    def getUserWalk(self):
        url = "hm/getUserWalk"
        dict = {}
        resp = self.post(url, dict)

    # 获取绑定设备信息
    @task(0)
    def getDeviceBindInfo(self):
        url = "hm/getDeviceBindInfo"
        dict = {"userId": self._userid}
        resp = self.post(url, dict)

    # 提交用户步行信息
    @task(0)
    def addUserWalk(self):
        url = "hm/addUserWalk"
        w={"recordTime": "2017-10-20 10:05:05",
            "walkNumber": "10000"
            }
        w=collections.OrderedDict(sorted(w.items(), key=lambda t: t[0]))
        walklist=[w]
        dict = {"walkList": walklist}
        resp = self.post(url, dict)

    # 获取用户城市
    @task(0)
    def getUserCity(self):
        url = "10010/getUserCity"
        dict = {"cityLat": "30.285207",
                "cityLng": "120.017538",
                "phoneNumber": self._phonenum,
                "userCityName": u"杭州市"}
        resp = self.post(url, dict)

    # 检查手机是否认证
    @task(0)
    def checkPhoneIsAuth(self):
        url = "10010/checkPhoneIsAuth"
        dict = {"phoneNumber": self._phonenum}
        resp = self.post(url, dict)

    # 统计未预约体检套餐
    @task(0)
    def countMyNwcNoBespeak(self):
        url = "10009/countMyNwcNoBespeak"
        dict = {}
        resp = self.post(url, dict)

    # 获取未读消息
    @task(0)
    def getUnreadMessageList(self):
        url = "10007/getUnreadMessageList"
        dict = {}
        resp = self.post(url, dict)

    # 检查红点
    @task(0)
    def checkNoticeRedPoint(self):
        url = "10007/checkNoticeRedPoint"
        dict = {}
        resp = self.post(url, dict)

    # 获取首页活动位
    @task(0)
    def getHomeActivity(self):
        url = "mall/getHomeActivity"
        dict = {"userId": self._userid}
        resp = self.post(url, dict)

    # 获取电话解读状态
    @task(0)
    def getTelServiceLastState(self):
        url = "10005/getTelServiceLastState"
        dict = {}
        resp = self.post(url, dict)

    # 获取家人列表
    @task(0)
    def getMyFamilyMemberList(self):
        url = "10002/getMyFamilyMemberList"
        dict = {}
        resp = self.post(url, dict)

    # 获取用户信息
    @task(0)
    def getMyUserInfo(self):
        url = "10001/getMyUserInfo"
        dict = {}
        resp = self.post(url, dict)

    # 获取自定义配置
    @task(0)
    def getCustomizedConfigList(self):
        url = "10001/getCustomizedConfigList"
        dict = {}
        resp = self.post(url, dict)

    # 获取首页推荐商品
    @task(0)
    def getHomeGoodsListByBigData(self):
        if self._userid:
            url = "mall/getHomeGoodsListByBigData"
            dict = {"cityCode": "330100", "phoneNumber": self._phonenum, "userId": self._userid, "needRefresh": 0}
            resp = self.post(url, dict)

    # 获取服务组织
    @task(0)
    def getMyServiceOrganizations(self):
        url = "10005/getMyServiceOrganizations"
        dict = {}
        resp = self.post(url, dict)

    # 咨讯首页
    @task(0)
    def homeinfo(self):
        url = "info/information/v480/getHomeInformation"
        dict = {"appVersion": "4.8.0", "pageSize": "5", "needCategory": "1"}
 #       dict = {"pageSize": "5"}
        resp = self.post(url, dict)

    # 获取popup版本
    @task(0)
    def getPopupVersion(self):
        url = "10007/getPopupVersion"
        dict = {"appVersion": "4.7.0"}
        resp = self.post(url, dict)

    # 视频推荐
    @task(0)
    def video_homeRecommendList(self):
        url = "video/homeRecommendList"
        dict = {}
        resp = self.post(url, dict)

    # 获取字典列表1
    @task(0)
    def getDictionaryList1(self):
        url = "10007/getDictionaryList"
        dict = {"category": 1, "userId": self._userid}
        resp = self.post(url, dict)

    # 获取字典列表2
    @task(0)
    def getDictionaryList2(self):
        url = "10007/getDictionaryList"
        dict = {"category": 2, "userId": self._userid}
        resp = self.post(url, dict)

    # 获取字典1
    @task(0)
    def getDic1(self):
        url = "10010/getDic"
        dict = {"dicName": "employeeAuthType", "userId": self._userid}
        resp = self.post(url, dict)

    # 获取字典2
    @task(0)
    def getDic2(self):
        url = "10010/getDic"
        dict = {"dicName": "refundType", "userId": self._userid}
        resp = self.post(url, dict)

    # 获取logo
    @task(0)
    def getCheckCompanyLogoList(self):
        url = "10007/getCheckCompanyLogoList"
        dict = {"userId": self._userid}
        resp = self.post(url, dict)

    # 检查升级
    @task(0)
    def checkUpdate(self):
        url = "10007/checkUpdate"
        dict = {"appType": 2, "appVersion": "4.7.0", "currentVersion": "4.7.0"}
        resp = self.post(url, dict)

    # 上传resistrationId
    @task(0)
    def uploadJpushRegistrationId(self):
        url = "10001/uploadJpushRegistrationId"
        dict = {"registrationId": "120c83f7601322b909c"}
        resp = self.post(url, dict)

    @task(0)
    # 首页最新更新商品
    def getNewUpdateGoods(self):
        url = "mall/getNewUpdateGoods"
        dict = {"cityCode": "330100", "pageIndex": 1, "pageSize": 10}
        resp = self.post(url, dict)

    # BI资讯详情
    @task(0)
    def bi_info_view(self):
        url="bi/userBehavior/upload"
        dict={
            "_from": "yjk",
            "actObj": self._informationId,
            "appVersion": "4.7.0",
            "bhvAmt": 0.0,
            "bhvCnt": 1,
            "bhvType": "view",
            "content": "",
            "from": "android",
            "objType": "info",
            "systemName": "PRO+6",
            "systemVersion": "7.1.1",
            "traceId": "%E9%A6%96%E9%A1%B5",
            "isTest": True,
            "userId": self._userid,
            "uuid": "9de1c3d4274e7693452598be729fd147a71e0a32"
        }
        resp=self.post(url,dict)

    # 商品详情
    @task(0)
    def getGoodsDetail(self):
        url="10010/getGoodsDetail"
        dict={
                "appVersion": "4.7.0",
                "cityCode": "330100",
                "goodsId": self._goodsId,
                "lat": "30.287269",
                "lng": "120.0221",
                "phoneNumber": self._phonenum
            }
        resp=self.post(url,dict)

    # 购物车数量
    @task(0)
    def getShoppingCartNum(self):
        url="10010/getShoppingCartNum"
        dict={}
        resp=self.post(url,dict)

    # 获取组合售卖列表
    @task(0)
    def getGoodsGroupPage(self):
        url="ec/getGoodsGroupPage"
        dict={
                "goodsId": self._goodsId,
                "pageIndex": 1, "pageSize": 1}
        resp=self.post(url,dict)

    # 资讯详情
    @task(0)
    def getInformationById(self):
        url = "info/information/getInformationById"
        dict = {"appVersion": "4.8.0", "informationId": self._informationId}
        resp = self.post(url, dict)

    # 查询点赞
    @task(0)
    def findupvote(self):
        url = "disc/findUpVote"
        dict = {"informationId": self._informationId}
        resp = self.post(url, dict)

    # 推荐资讯列表
    @task(0)
    def recommendationInfoList(self):
        url = "info/information/recommendationInfoList"
        dict = {"informationId": self._informationId}
        resp = self.post(url, dict)


    # APP获取首页视频列表
    @task(0)
    def video_v490_home_recommend_list(self):
        url = 'video/v490/homeRecommendList'
        dict = {}
        resp = self.post(url, dict)

    # 获取电话解读历史状态
    @task(0)
    def getTelServiceLastStateHistory(self):
        url = "health/getTelServiceLastStateHistory"
        dict = {"appVersion": "4.8.0", "userId": self._userid}
        resp = self.post(url, dict)

    # 加载资讯详情
    @task(0)
    def openinfo(self):
        self.getInformationById()
        self.recommendationInfoList()
        self.findupvote()
        self.bi_info_view()

    # 加载商品详情
    @task(0)
    def opengoods(self):
        self.getShoppingCartNum()
        self.getGoodsDetail()
        self.getGoodsGroupPage()

    # 加载首页
    @task(1)
    def home(self):
        self.checkUpdate()
        self.getUnreadMessageList()
        self.getNewUpdateGoods()
        self.getMyFamilyMemberList()
        self.homeinfo()
        self.getUserWalk()
        self.getHomeGoodsListByBigData()
        self.getHomeActivity()
        self.getMyUserInfo()
        self.getPopupVersion()
        self.checkNoticeRedPoint()
        self.countMyNwcNoBespeak()
        self.addUserWalk()
        self.getUserCity()
        self.video_v490_home_recommend_list()
        self.getTelServiceLastStateHistory()

        # self.video_homeRecommendList()
        # self.getDeviceBindInfo()
        # self.getTelServiceLastState()
        # self.getUserCardInfo()
        # self.checkPhoneIsAuth()
        # self.getCustomizedConfigList()
        # self.getDictionaryList1()
        # self.getDictionaryList2()
        # self.getDic1()
        # self.getDic2()
        # self.getCheckCompanyLogoList()
        # self.bi_userBehavior_upload()
        # self.getMyServiceOrganizations()
        # self.uploadJpushRegistrationId()

    # 添加报告
    @task(0)
    def addreport(self):
        url = "10005/addReportByCID"
        dict = {"healthCompanyCode": "20001", "password": "584113", "reportId": "1826116"}
        resp = self.post(url, dict)

    # 视频详情
    @task(0)
    def video_getVideoDetail(self):
        url="video/getVideoDetail"
        dict={"videoId": "502"}
        resp=self.post(url,dict)
