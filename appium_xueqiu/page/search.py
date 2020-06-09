# _*_ coding:utf-8 _*_
# @Time: 2020/6/713:50
# @Author: Jerry
from appium_xueqiu.page.basepage import BasePage


class Search(BasePage):
    def search(self, text, name):
        # 替换配置文件中的变量
        self._params["text"] = text
        self._params["name"] = name
        self.steps("search.yaml")

    def add(self, name):
        self._params["name"] = name
        self.steps("search.yaml")

    def is_choose(self, name):
        self._params["name"] = name
        return self.steps("search.yaml")

    def reset(self, name):
        self._params["name"] = name
        return self.steps("search.yaml")
