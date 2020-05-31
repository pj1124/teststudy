# _*_ coding:utf-8 _*_
# @Time: 2020/5/2421:27
# @Author: Jerry

from wework.pages.base_page import BasePage


class AddManually(BasePage):

    def input_name(self, name):
        self.d(resourceId="com.tencent.wework:id/au7", text="必填").send_keys(name)

    def select_gender(self, gender):
        self.d(resourceId="com.tencent.wework:id/av1", text="男").click()
        self.d(resourceId="com.tencent.wework:id/drb", text=gender).click()

    def input_phone(self, phone):
        self.d(resourceId="com.tencent.wework:id/eqx").send_keys(phone)

    def save_member(self):
        self.d(resourceId="com.tencent.wework:id/gvl").click()
        self.d.implicitly_wait(15)

    def back(self):
        self.d(resourceId="com.tencent.wework:id/gv3").click()

    def toast(self):
        toast = self.d.toast.get_message(15.0, default="")
        return toast