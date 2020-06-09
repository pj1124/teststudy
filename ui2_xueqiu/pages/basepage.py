# _*_ coding:utf-8 _*_
# @Time: 2020/5/3016:16
# @Author: Jerry

import uiautomator2 as u2


class BasePage:

    def __init__(self):
        self.d = u2.connect('127.0.0.1:7555')
        self.d.app_start('com.ui2_xueqiu.android')
        self.d.implicitly_wait(15)

    def app_stop(self):
        return self.d.app_stop('com.ui2_xueqiu.android')

    # 重写元素定位方法
    def element(self, dic):
        return self.d(**dic)

    # 重写定位元素右边的元素方法
    def element_right(self, dic1, dic2):
        return self.element(dic1).right(**dic2)

    # 重写定位元素左边的元素方法
    def element_left(self, dic1, dic2):
        return self.element(dic1).right(**dic2)

    # 重写定位元素上面的元素方法
    def element_up(self, dic1, dic2):
        return self.element(dic1).right(**dic2)

    # 重写定位元素下面的元素方法
    def element_down(self, dic1, dic2):
        return self.element(dic1).right(**dic2)

    # 获取toast方法
    def get_toast_message(self):
        toast = self.d.toast.get_message(5.0, default="")
        return toast
