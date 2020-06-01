# _*_ coding:utf-8 _*_
# @Time: 2020/5/3016:18
# @Author: Jerry
from xueqiu.confing.yaml import Config
from xueqiu.pages.basepage import BasePage


class Search(BasePage):

    send_key = Config().read_data('search')['send_key']
    text_1 = Config().read_data('search')['text_1']
    text_2 = Config().read_data('search')['text_2']
    adding = Config().read_data('search')['adding']
    cancel = Config().read_data('search')['cancel']

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
