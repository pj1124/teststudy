# _*_ coding:utf-8 _*_
# @Time: 2020/5/3016:17
# @Author: Jerry
from ui2_xueqiu.confing.yaml import Config
from ui2_xueqiu.pages.basepage import BasePage
from ui2_xueqiu.pages.search_page import Search


class Market(BasePage):

    search = Config().read_data('market')['search']

    def click_search(self):
        self.element(self.search).click()
        return Search()
