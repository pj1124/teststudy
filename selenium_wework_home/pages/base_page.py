# _*_ coding:utf-8 _*_
# @Time: 2020/5/1716:30
# @Author: Jerry

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        # 如果没传driver方法，则复用当前浏览器窗口，否则就重新打开浏览器
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
            self._driver.maximize_window()
            self._driver.implicitly_wait(3)

        else:
            self._driver = driver
            self._driver.maximize_window()
            self._driver.implicitly_wait(3)

        if self._base_url != "":
            self._driver.get(self._base_url)

    # 重写元素定位方法
    def find(self, *loc):
        try:
            # 显示等待时间为5秒，并且检查元素是否存在以及元素是否可见
            element = WebDriverWait(self._driver, 3).until(
                ec.element_to_be_clickable(*loc)
            )
            return element
        except:
           print("找不到元素"+str(loc))

    def finds(self, *loc):
        try:
            # 显示等待时间为5秒，并且检查元素是否存在以及元素是否可见
            elements = WebDriverWait(self._driver, 10, 0.5).until(
                ec.visibility_of_all_elements_located(*loc)
            )
            return elements
        except:
           print("找不到元素:"+str(loc))

    # 重写元素点击方法
    def click(self,element):
        self.find(element).click()

    # 重写输入值的方法
    def send_keys(self, loc, keys, clear=True):
        try:
            if clear:
                self.find(loc).clear()
                self.find(loc).send_keys(keys)
        except AttributeError:
            print(u"输入错误:"+str(loc)+keys)




