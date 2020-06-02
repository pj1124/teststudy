# _*_ coding:utf-8 _*_
# @Time: 2020/6/221:39
# @Author: Jerry
from xueqiu.confing.yaml import Config
from xueqiu.pages.basepage import BasePage


class Watcher(BasePage):

    def open_watcher(self):
        alert_list = Config().read_data('blacklist')['blacklist']
        for alert in alert_list:
            self.d.watcher.when(xpath=alert).click()
        self.d.watcher.start()

    def close_watcher(self):
        # 关闭观察者
        self.d.watcher.remove()
