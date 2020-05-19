# _*_ coding:utf-8 _*_
# @Time: 2020/5/1722:37
# @Author: Jerry

from time import sleep
from selenium_wework_home.case.add_member import AddMember
from selenium_wework_home.case.delete_member import DeleteMember


class TestAddMember:

    def setup(self):
        # 实例化AddMember类
        self.add_member = AddMember()
        # 实例化DeleteMember类
        self.delete_member = DeleteMember()

    def teardown(self):
        sleep(2)
        # 删除添加的成员
        self.delete_member.delete_member()

    def test_add_member(self):
        # 添加成员
        self.add_member.add_member()



