# _*_ coding:utf-8 _*_
# @Time: 2020/6/713:49
# @Author: Jerry

from appium_xueqiu.page.basepage import BasePage
from appium_xueqiu.page.search import Search


class Market(BasePage):
    def click_search(self):
        self.steps("market.yaml")
        return Search(self._driver)
