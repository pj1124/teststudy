# _*_ coding:utf-8 _*_
# @Time: 2020/5/2421:23
# @Author: Jerry
from time import sleep

from wework.pages.add_manually import AddManually
from wework.pages.base_page import BasePage


class AddMember(BasePage):

    def add_manually(self):
        sleep(3)
        self.d(text="手动输入添加").click()
        return AddManually()