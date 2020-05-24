# _*_ coding:utf-8 _*_
# @Time: 2020/5/1720:24
# @Author: Jerry

from selenium.webdriver.common.by import By
from selenium_wework_home.pages.base_page import BasePage
from selenium_wework_home.pages.login_page import LoginPage
from selenium_wework_home.pages.register_page import RegisterPage


class IndexPage(BasePage):

    login_loc = (By.CSS_SELECTOR, '.index_top_operation_loginBtn')
    register_loc = (By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn')

    def login_click(self):
        self.click(self.login_loc)
        return LoginPage()

    def register_click(self):
        self.click(self.register_loc)
        return RegisterPage()
