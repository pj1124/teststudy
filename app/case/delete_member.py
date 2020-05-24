# _*_ coding:utf-8 _*_
# @Time: 2020/5/2422:38
# @Author: Jerry

from app.pages.address_list import AddressList
from app.pages.edit_member import EditMember
from app.pages.main import Main
from app.pages.member_details import MemberDetails
from app.pages.member_details_operation import MemberDetailsOperation


class DeleteContacts:

    def __init__(self):
        self.main = Main()
        self.address_list = AddressList()
        self.click_operation = MemberDetails()
        self.operation = MemberDetailsOperation()
        self.edit = EditMember()

    def delete_contacts(self, name):
        delete = self.main.click_address_list().select_member(name).click_operation().edit_member()
        delete.delete_member()
        delete.click_popup_ok()
        self.main.click_message()
