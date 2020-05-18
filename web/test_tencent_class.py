# _*_ coding:utf-8 _*_
# @Time: 2020/5/1320:23
# @Author: Jerry

import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestTencentClass:
    """
    使用cookie登录web网站
    """

    def setup(self):
        options = Options()
        # options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_tencent_class(self):
        self.driver.get('https://ke.qq.com/')
        # Shelve是对象持久化保存方法，将对象保存到文件里面，可以作为一个简单的数据存储方案。
        db = shelve.open("cookies")
        # db['cookie'] = self.driver.get_cookies()
        # print(self.driver.get_cookies())
        cookies = db['cookie']
        # 从保存的cookies文件中将cookie取出来，并去除expiry的值后，添加到driver中
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://ke.qq.com/')
        # self.driver.find_element_by_id('js_login').click()
        sleep(5)
        js = "document.getElementsByClassName('btn-outline main-category-cancel js-intrest-cancel')[0].click()"
        self.driver.execute_script(js)
        sleep(5)
        db.close()





