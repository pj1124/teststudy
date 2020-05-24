# _*_ coding:utf-8 _*_
# @Time: 2020/5/1716:09
# @Author: Jerry


from selenium.webdriver.common.by import By
from selenium_wework_home.pages.base_page import BasePage
from selenium_wework_home.pages.add_member_page import AddMemberPage
from selenium_wework_home.pages.delete_member_page import DeleteMemberPage


class ContactsPage(BasePage):

    add_member_loc = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
    delete_member_loc = (By.CSS_SELECTOR, '.js_delete')

    def click_add_member(self):
        self.click(self.add_member_loc)
        return AddMemberPage()

    def click_delete_member(self):
        self.click(self.delete_member_loc)
        return DeleteMemberPage()