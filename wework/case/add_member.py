# _*_ coding:utf-8 _*_
# @Time: 2020/5/2421:39
# @Author: Jerry


from wework.pages.main import Main


class AddContacts:

    def __init__(self):
        self.main = Main()

    def add_contacts(self, name, gender, phone):
        add = self.main.click_address_list().add_member().add_manually()
        add.input_name(name)
        add.select_gender(gender)
        add.input_phone(phone)
        add.save_member()
        add.back()
        self.main.click_message()
