# _*_ coding:utf-8 _*_
# @Time: 2020/5/3016:17
# @Author: Jerry

from xueqiu.pages.basepage import BasePage
from xueqiu.pages.search_page import Search


class Market(BasePage):

    search = {'resourceId': 'com.xueqiu.android:id/action_search'}

    def click_search(self):
        self.element(self.search).click()
        return Search()
