# _*_ coding:utf-8 _*_
# @Time: 2020/5/2420:19
# @Author: Jerry


import uiautomator2 as u2


class BasePage:

    def __init__(self):
        self.d = u2.connect('127.0.0.1:7555')
        self.d.app_start('com.tencent.wework')
        self.d.implicitly_wait(5)