# _*_ coding:utf-8 _*_
# @Time: 2020/5/1721:04
# @Author: Jerry

from selenium.webdriver.common.by import By
from selenium_wework_home.pages.base_page import BasePage
from selenium_wework_home.pages.register_page import RegisterPage


class LoginPage(BasePage):

    register_loc = (By.CSS_SELECTOR, '.login_registerBar_link')

    def register_click(self):
        self.click(self.register_loc)
        return RegisterPage(self._driver)