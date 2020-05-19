# _*_ coding:utf-8 _*_
# @Time: 2020/5/1921:40
# @Author: Jerry

from selenium.webdriver.common.by import By
from selenium_wework_home.case.check_menber import CheckMember
from selenium_wework_home.pages.base_page import BasePage
from selenium_wework_home.pages.contacts_page import ContactsPage
from selenium_wework_home.pages.delete_member_page import DeleteMemberPage


class DeleteMember(BasePage):

    def delete_member(self):
        element = CheckMember().check_box()
        loc = (By.CSS_SELECTOR, element)
        self.click(loc)
        ContactsPage().click_delete_member()
        DeleteMemberPage().click_delete_confirm()

