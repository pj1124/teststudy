# _*_ coding:utf-8 _*_
# @Time: 2020/5/2422:22
# @Author: Jerry

from wework.pages.base_page import BasePage
from wework.pages.member_details_operation import MemberDetailsOperation


class MemberDetails(BasePage):

    def click_operation(self):
        self.d(resourceId="com.tencent.wework:id/gvr").click()
        return MemberDetailsOperation()