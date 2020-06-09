# _*_ coding:utf-8 _*_
# @Time: 2020/5/3016:39
# @Author: Jerry

from ui2_xueqiu.confing.yaml import Config
from ui2_xueqiu.pages.basepage import BasePage
from ui2_xueqiu.pages.market_page import Market


class Main(BasePage):
    marker = Config().read_data('main')['marker']

    def click_market(self):
        self.element(self.marker).click()
        return Market()
