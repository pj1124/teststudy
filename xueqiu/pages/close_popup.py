# _*_ coding:utf-8 _*_
# @Time: 2020/6/123:03
# @Author: Jerry

from time import sleep
from xueqiu.pages.basepage import BasePage


class ClosePopup(BasePage):

    def watchers(self, text, func):
        try:
            func()
        except Exception:
            self.d.watcher("WATCHER_NAME").when(text=text).click(text=text)
            self.d.watchers.watched = True
            sleep(2)
            self.d.watchers.remove()
            func()
