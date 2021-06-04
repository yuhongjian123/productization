"""
浏览器工具
"""

from selenium import webdriver
from time import sleep


class DriverTool(object):
    driver = None  # 初始化浏览器

    @classmethod
    def get_driver(cls):
        if cls.driver is None:  # 判断浏览器是否为空
            cls.driver = webdriver.Chrome()
            url = 'http://172.16.101.21:15001/login'
            cls.driver.get(url)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver  # 返回浏览器对象

    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None


if __name__ == '__main__':
    DriverTool.get_driver()
    sleep(5)
    DriverTool.quit_driver()
