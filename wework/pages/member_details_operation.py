# _*_ coding:utf-8 _*_
# @Time: 2020/5/2422:25
# @Author: Jerry

from wework.pages.base_page import BasePage
from wework.pages.edit_member import EditMember
# from wework.pages.member_details import MemberDetails


class MemberDetailsOperation(BasePage):

    def edit_member(self):
        self.d(resourceId="com.tencent.wework:id/azk").click()
        return EditMember()