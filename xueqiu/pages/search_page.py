# _*_ coding:utf-8 _*_
# @Time: 2020/5/3016:18
# @Author: Jerry

from xueqiu.pages.basepage import BasePage


class Search(BasePage):

    send_key = {'resourceId': 'com.xueqiu.android:id/search_input_text'}
    text_1 = {'resourceId': 'com.xueqiu.android:id/code', 'text': 'BABA'}
    text_2 = {'resourceId': 'com.xueqiu.android:id/stockCode', 'text': 'BABA'}
    adding = {'text': '加自选'}
    cancel = {'text': '已添加'}

    def send(self,keys, t):
        self.element(self.send_key).send_keys(keys)
        self.text_1['text'] = t
        self.element(self.text_1).click()

    def click_adding(self, t):
        self.text_2['text'] = t
        self.element_right(self.text_2, self.adding).click()

    def click_cancel_adding(self, t):
        self.text_2['text'] = t
        self.element_right(self.text_2, self.cancel).click()
