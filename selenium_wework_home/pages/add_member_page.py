# _*_ coding:utf-8 _*_
# @Time: 2020/5/1722:08
# @Author: Jerry

from selenium.webdriver.common.by import By
from selenium_wework_home.pages.base_page import BasePage


class AddMemberPage(BasePage):

    username_loc = (By.ID, 'username')
    acctid_loc = (By.ID, 'memberAdd_acctid')
    phone_loc = (By.ID, 'memberAdd_phone')
    title_loc = (By.ID, 'memberAdd_title')
    save_loc = (By.ID, '.js_btn_save')

    def input_username(self):
        self.send_keys(self.username_loc,'test01')

    def input_acctid(self):
        self.send_keys(self.acctid_loc,'100100')

    def input_phone(self):
        self.send_keys(self.phone_loc,'18188888888')

    def input_title(self):
        self.send_keys(self.title_loc,'CTO')

    def click_save(self):
        self.click(self.save_loc)
