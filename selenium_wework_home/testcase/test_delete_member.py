# _*_ coding:utf-8 _*_
# @Time: 2020/5/201:27
# @Author: Jerry

from time import sleep
from selenium_wework_home.case.check_menber import CheckMember
from selenium_wework_home.case.delete_member import DeleteMember


class TestDeleteMember:
    """
    删除成员
    """

    def setup(self):
        # 实例化DeleteMember类
        self.delete_member = DeleteMember()
        # 实例化CheckMember类
        self.check_member = CheckMember()

    def test_delete_member(self):
        # 删除添加的成员
        self.delete_member.delete_member()
        sleep(1)
        text = self.check_member.members_list_text()
        assert "test01" not in text, "删除成员失败"