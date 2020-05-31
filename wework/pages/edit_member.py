# _*_ coding:utf-8 _*_
# @Time: 2020/5/2422:30
# @Author: Jerry

from wework.pages.base_page import BasePage


class EditMember(BasePage):

    def delete_member(self):
        self.d(resourceId="com.tencent.wework:id/dve").click()

    def click_popup_ok(self):
        self.d(resourceId="com.tencent.wework:id/b_a").click()
        self.d.implicitly_wait(15)

