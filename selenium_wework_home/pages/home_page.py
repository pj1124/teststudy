# _*_ coding:utf-8 _*_
# @Time: 2020/5/1715:50
# @Author: Jerry


from selenium.webdriver.common.by import By
from selenium_wework_home.pages.base_page import BasePage
from selenium_wework_home.pages.contacts_page import ContactsPage


class HomePage(BasePage):

    home_loc = (By.ID, 'menu_index')
    contacts_loc = (By.ID, 'menu_contacts')
    apps_loc = (By.ID, 'menu_apps')
    customer_loc = (By.ID, 'menu_customer')
    manageTools_loc = (By.ID, 'menu_manageTools')
    profile_loc = (By.ID, 'menu_profile')

    def click_home(self):
        self.click(self.home_loc)
        return HomePage()

    def click_contacts(self):
        self.click(self.contacts_loc)
        return ContactsPage()

    def click_apps(self):
        self.click(self.apps_loc)
        pass

    def click_customer(self):
        self.click(self.customer_loc)
        pass

    def click_manageTools(self):
        self.click(self.manageTools_loc)
        pass

    def click_profile(self):
        self.click(self.profile_loc)
        pass