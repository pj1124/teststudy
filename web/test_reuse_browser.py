# _*_ coding:utf-8 _*_
# @Time: 2020/5/1610:14
# @Author: Jerry

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestReuseBrowser:
    """
    浏览器复用
    1、需要将Chrome加入环境变量
    2、运行时需要关闭后台Chrome进程
    3、cmd执行命令“chrome --remote-debugging-port=9222”打开调试模式，并且端口号要与脚本一致
    """
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_reuse_browser(self):
        # # 点击近期里面的创建新主题
        self.driver.find_element_by_xpath('//*[@id="create-topic"]/span').click()
        sleep(3)


