# _*_ coding:utf-8 _*_
# @Time: 2020/6/720:58
# @Author: Jerry

import pytest
from appium_xueqiu.common.app import App
from appium_xueqiu.common.operation_yaml import read_date


class TestSearch:
    data_list = read_date("search_data.yaml")

    def setup(self):
        self.search = App().start().main().click_market().click_search()

    @pytest.mark.parametrize("text, name", data_list)
    def test_search(self, text, name):
        self.search.search(text, name)
        if self.search.is_choose(name):
            self.search.reset(name)
        self.search.add(name)
        assert self.search.is_choose(name)
