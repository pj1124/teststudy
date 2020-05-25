# _*_ coding:utf-8 _*_
# @Time: 2020/5/2421:46
# @Author: Jerry
from time import sleep

import pytest
from app.case.add_member import AddContacts
from app.case.delete_member import DeleteContacts
from app.common.operation_elements import Elements
from app.pages.add_manually import AddManually


class TestOperationMember:

    def setup_class(self):
        self.add_contacts = AddContacts()
        self.delete_contacts = DeleteContacts()

    data_list = [("test01", "男", "18112340001"), ("test02", "女", "18112340002"), ("test03", "男", "18112340003"),
                 ("test04", "女", "18112340004"), ("test05", "男", "18112340005"), ("test06", "女", "18112340006")]

    name_list = ["test01", "test02", "test03", "test04", "test05", "test06"]

    @pytest.mark.parametrize('name, gender, phone', data_list)
    def test_add_member(self, name, gender, phone):
        self.add_contacts.add_contacts(name, gender, phone)
        self.toast = AddManually().toast()
        assert "添加成功" in self.toast, "成员添加失败"

    @pytest.mark.parametrize('name', name_list)
    def test_delete_member(self, name):
        self.delete_contacts.delete_contacts(name)
        assert Elements().get_element_text(name) == -32002
