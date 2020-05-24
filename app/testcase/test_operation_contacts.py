# _*_ coding:utf-8 _*_
# @Time: 2020/5/2421:46
# @Author: Jerry

import pytest
from app.case.add_member import AddContacts
from app.case.delete_member import DeleteContacts
from app.pages.add_manually import AddManually


class TestOperationMember:

    def setup_class(self):
        self.add_contacts = AddContacts()
        self.delete_contacts = DeleteContacts()

    data_list = [("test01", "男", "18112340001"), ("test02", "女", "18112340002"), ("test03", "女", "18112340003"),
                 ("test04", "男", "18112340004")]

    @pytest.mark.parametrize('name, gender, phone', data_list)
    def test_add_member(self, name, gender, phone):
        self.add_contacts.add_contacts(name, gender, phone)
        self.toast = AddManually().toast()
        assert "添加成功" in self.toast, "成员添加失败"

    name_list = ["test01", "test02", "test03", "test04"]

    @pytest.mark.parametrize('name', name_list)
    def test_delete_member(self, name):
        self.delete_contacts.delete_contacts(name)
