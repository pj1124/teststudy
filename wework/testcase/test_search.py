# _*_ coding:utf-8 _*_
# @Time: 2020/5/2310:30
# @Author: Jerry


import pytest
import uiautomator2 as u2


class TestSearch:

    def setup(self):
        self.d = u2.connect('127.0.0.1:7555')
        self.d.app_start('com.xueqiu.android')

    def teardown(self):
        self.d.app_stop('com.xueqiu.android')

    @pytest.mark.parametrize('text', ['阿里巴巴', '京东', '百度'])
    def test_search(self, text):
        # self.d.implicitly_wait(15)
        # self.d(resourceId="com.xueqiu.android:id/tv_skip_fullscreen").click()
        self.d.implicitly_wait(15)
        self.d(resourceId="com.xueqiu.android:id/home_search").click()
        self.d.implicitly_wait(15)
        self.d(resourceId="com.xueqiu.android:id/search_input_text").send_keys(text)
        self.d.implicitly_wait(15)
        self.d(resourceId="com.xueqiu.android:id/name", text="%s" % (text)).click()
        self.d.implicitly_wait(15)
        self.d(resourceId="com.xueqiu.android:id/stockName", text="%s" % (text)).right(resourceId="com.xueqiu.android:id/add_attention").click()
        assert "添加成功" in self.d.toast.get_message(15.0, default="")




