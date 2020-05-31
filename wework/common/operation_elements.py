# _*_ coding:utf-8 _*_
# @Time: 2020/5/2521:05
# @Author: Jerry

from wework.pages.base_page import BasePage


class Elements(BasePage):

    def find_by_text(self, text):
        return self.d(text=text)

    def find_by_id(self, resourceId):
        return self.d(resourceId=resourceId)

    def find_by_class(self, className):
        return self.d(className=className)

    def find_by_xpath(self, xpath):
        return self.d.xpath(xpath)

    def find_id_text(self, resourceId, text):
        return self.d(resourceId=resourceId, text=text)

    def find_id_class(self, resourceId, className):
        return self.d(resourceId=resourceId, className=className)

    def find_class_text(self, resourceId, text):
        return self.d(resourceId=resourceId, text=text)

    def get_element_text(self, element):
        try:
            text = self.d(text=element).get_text()
            return text
        except Exception as error:
            return error.args[0]['code']

