# -*- coding: UTF-8 -*-

from locust import HttpLocust
import Queue
import logging
import datetime
import os
from yjktask import YJKTask
#from live import YJKTask

class YJKUser(HttpLocust):
    # 设置Locust压力测试主机地址，用户任务类
    # host = "http://rapapi-test2.ihaozhuo.com:82/"
    host = "http://restapi-gray.ihaozhuo.com/"
    # host = "http://120.26.164.77:8080/"
    # host = "http://192.168.1.182:10002/"
    task_set = YJKTask

    # 设置日志文件及格式
    if not os.path.exists('./log'):
        os.mkdir('./log')
    logging.basicConfig(level=logging.INFO)
    fh = logging.FileHandler('./log/log_%s.txt' % datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), mode='w')
    formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger = logging.getLogger()    #__name__)
    logger.addHandler(fh)

    # 测试环境帐号，用队列管理，确保并发使用且不重复：
    user_queue=Queue.Queue()
    for index in range(10000):
        user_queue.put(14312100000 + index)

    # 用户测试场景的等待时间ms，随机时间在min和max之间
    min_wait = 0000
    max_wait = 0000
    # 压测时间s，到时自动停止
    # stop_timeout = 600
