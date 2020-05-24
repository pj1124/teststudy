# _*_ coding:utf-8 _*_
# @Time: 2020/5/2420:15
# @Author: Jerry

from app.pages.add_member import AddMember
from app.pages.base_page import BasePage
from app.pages.member_details import MemberDetails


class AddressList(BasePage):

    def add_member(self):
        self.d(text="添加成员").click()
        return AddMember()

    def select_member(self, name):
        self.d(text=name).click()
        return MemberDetails()