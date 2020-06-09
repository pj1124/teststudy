# _*_ coding:utf-8 _*_
# @Time: 2020/6/713:43
# @Author: Jerry

from appium import webdriver
from appium_xueqiu.page.main import Main
from appium_xueqiu.page.basepage import BasePage


class App(BasePage):
    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps['noReset'] = "true"
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(3)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
