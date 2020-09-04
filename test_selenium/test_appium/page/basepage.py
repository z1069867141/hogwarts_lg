"""
基类：存放一些最基本的方法，最通用方法
实例化 driver,find,back,home......
"""
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver=None):
        """
        初始化driver
        """
        self.driver = driver