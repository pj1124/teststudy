# _*_ coding:utf-8 _*_
# @Time: 2020/5/3018:35
# @Author: Jerry

import pytest

from xueqiu.pages.basepage import BasePage
from xueqiu.pages.main_page import Main
from xueqiu.pages.watcher import Watcher


class TestSearch:
    data_list = [('阿里巴巴', 'BABA'), ('京东', 'JD'), ('百度', 'BIDU'), ('腾讯控股ADR', 'TCEHY')]

    def setup_class(self):
        self.base_page = BasePage()
        Watcher().open_watcher()

    def teardown_class(self):
        self.base_page.app_stop()
        Watcher().close_watcher()

    @pytest.mark.parametrize('company, code', data_list)
    def test_adding(self, company, code):
        a = Main().click_market().click_search()
        a.send(company, code)
        a.click_adding(code)
        assert "添加成功" in self.base_page.get_toast_message()

    @pytest.mark.parametrize('company, code', data_list)
    def test_cancel_adding(self, company, code):
        a = Main().click_market().click_search()
        a.send(company, code)
        a.click_cancel_adding(code)
        assert "已从自选删除" in self.base_page.get_toast_message()
