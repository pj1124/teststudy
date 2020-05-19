# _*_ coding:utf-8 _*_
# @Time: 2020/5/1722:44
# @Author: Jerry


from time import sleep
from selenium_wework_home.pages.home_page import HomePage


class AddMember:

    def add_member(self):
        # 点击通讯录
        click_contacts = HomePage().click_contacts()
        # 点击添加成员
        sleep(2)
        click_add_member = click_contacts.click_add_member()
        # 输入基本信息
        click_add_member.input_username()
        click_add_member.input_acctid()
        click_add_member.input_phone()
        click_add_member.input_title()
        # 点击保存
        click_add_member.click_save()
