# _*_ coding:utf-8 _*_
# @Time: 2020/5/2420:16
# @Author: Jerry

from wework.pages.address_list import AddressList
from wework.pages.base_page import BasePage


class Main(BasePage):

    def click_message(self):
        self.d(resourceId="com.tencent.wework:id/drb", text="消息").click()

    def click_address_list(self):
        self.d(resourceId="com.tencent.wework:id/drb", text="通讯录").click()
        return AddressList()