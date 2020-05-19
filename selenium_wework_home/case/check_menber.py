# _*_ coding:utf-8 _*_
# @Time: 2020/5/200:42
# @Author: Jerry

from selenium.webdriver.common.by import By

from selenium_wework_home.pages.base_page import BasePage


class CheckMember(BasePage):
    """
    默认成员列表只有一页显示，暂不考虑分页场景
    """

    def get_currpage_members_number(self):
        """
        获取成员列表行数，即成员数量
        :return: 成员列表行数
        """
        loc = (By.CSS_SELECTOR, '.js_list>tr')
        elements = self.finds(loc)
        return len(elements)

    def members_list_text(self):
        """
        获取成员列表文字信息
        :return: 返回成员列表文字信息
        """
        loc = (By.CSS_SELECTOR, '.js_list')
        element_container = self.finds(loc)
        for words in element_container:
            text_container = words.text
            return text_container

    def check_box(self):
        """
        逐行检查列表成员
        :return: 目标成员定位元素
        """
        num = self.get_currpage_members_number()
        for i in range(num):
            i = i + 1
            ele = '.js_list>tr:nth-child(%s)' % (i)
            loc = (By.CSS_SELECTOR, ele)
            container = self.finds(loc)
            for words in container:
                member_info = words.text
                if 'test01' in member_info:
                    element = '.js_list>tr:nth-child(%s)>td:nth-child(1)' % (i)
                    return element
