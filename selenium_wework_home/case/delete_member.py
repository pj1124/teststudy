# _*_ coding:utf-8 _*_
# @Time: 2020/5/1921:40
# @Author: Jerry
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from selenium_wework_home.pages.base_page import BasePage
from selenium_wework_home.pages.contacts_page import ContactsPage
from selenium_wework_home.pages.delete_member_page import DeleteMemberPage


class DeleteMember(BasePage):

    def delete_member(self):
        i = 0
        while True:
            i = i + 1
            element =  '.js_list>tr:nth-child(%s)'%(i)
            loc = (By.CSS_SELECTOR, element)
            container = self.finds(loc)
            for words in container:
                member_info = words.text
                if 'test01' in member_info:
                    element = '.js_list>tr:nth-child(%s)>td:nth-child(1)' % (i)
                    loc = (By.CSS_SELECTOR, element)
                    self.click(loc)
                    ContactsPage().click_delete_member()
                    DeleteMemberPage().click_delete_confirm()
                    return True










if __name__=='__main__':
    DeleteMember().get_member()

