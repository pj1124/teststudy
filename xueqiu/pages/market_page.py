# _*_ coding:utf-8 _*_
# @Time: 2020/5/3016:17
# @Author: Jerry
from xueqiu.confing.yaml import Config
from xueqiu.pages.basepage import BasePage
from xueqiu.pages.search_page import Search


class Market(BasePage):

    search = Config().read_data('market')['search']

    def click_search(self):
        self.element(self.search).click()
        return Search()
