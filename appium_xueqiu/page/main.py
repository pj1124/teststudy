# _*_ coding:utf-8 _*_
# @Time: 2020/6/713:45
# @Author: Jerry

from appium_xueqiu.page.basepage import BasePage
from appium_xueqiu.page.market import Market


class Main(BasePage):
    def click_market(self):
        self.set_implicitly(10)
        self.steps("main.yaml")
        self.set_implicitly(3)
        return Market(self._driver)
