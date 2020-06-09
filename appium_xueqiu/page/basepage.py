# _*_ coding:utf-8 _*_
# @Time: 2020/6/713:34
# @Author: Jerry

import inspect
import json
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from appium_xueqiu.common.operation_yaml import read_date
from appium_xueqiu.page.wrapper import handle_black


class BasePage:
    # 定义公共变量区域用来存字典
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def set_implicitly(self, time):
        self._driver.implicitly_wait(time)

    def screenshot(self, name):
        self._driver.save_screenshot(name)

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    @handle_black
    def find_and_get_text(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text

    def steps(self, path):
        # 获取调用本函数的函数名称
        name = inspect.stack()[1].function
        # 读取配置文件中指定字典内容
        steps = read_date(path)[name]
        # 替换配置文件中的变量替换---> ${ }
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace('${' + key + '}', value)
        steps = json.loads(raw)
        # 循环遍历从配置文件中读取出来的字典内容，并进行解析
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "len > 0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0
