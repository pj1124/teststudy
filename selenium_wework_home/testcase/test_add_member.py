# _*_ coding:utf-8 _*_
# @Time: 2020/5/1722:37
# @Author: Jerry


from selenium_wework_home.case.add_member import AddMember
from selenium_wework_home.case.check_menber import CheckMember


class TestAddMember:
    """
    添加成员
    """

    def setup(self):
        # 实例化AddMember类
        self.add_member = AddMember()

    def test_add_member(self):
        # 添加成员
        self.add_member.add_member()
        text = CheckMember().members_list_text()
        assert "test01" in text, "成员添加失败"
