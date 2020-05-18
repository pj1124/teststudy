# _*_ coding:utf-8 _*_
# @Time: 2020/5/1722:44
# @Author: Jerry
from time import sleep

from selenium.webdriver.common.by import By

from selenium_wework_home.pages.add_member_page import AddMemberPage
from selenium_wework_home.pages.contacts_page import ContactsPage
from selenium_wework_home.pages.home_page import HomePage
from selenium_wework_home.pages.base_page import BasePage


class AddMember:
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def add_member(self):
        # 点击通讯录
        click_contacts = HomePage().click_contacts()
        # 点击添加成员
        click_add_member = click_contacts.click_add_member()
        # 输入基本信息
        click_add_member.input_username()
        click_add_member.input_acctid()
        click_add_member.input_phone()
        click_add_member.input_title()
        # 点击保存
        click_add_member.click_save()




