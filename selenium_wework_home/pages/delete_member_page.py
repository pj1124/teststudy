# _*_ coding:utf-8 _*_
# @Time: 2020/5/1722:28
# @Author: Jerry


from selenium.webdriver.common.by import By
from selenium_wework_home.pages.base_page import BasePage


class DeleteMemberPage(BasePage):

    confirm_loc = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')

    def click_delete_confirm(self):
        self.click(self.confirm_loc)