"""
基类：存放一些最基本的方法，最能用方法
实例化 driver,find,back,home,显示等待......
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        logging.info(locator)
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        logging.info("点击")
        self.find(locator).click()

    def find_by_scroll_and_click(self, text):
        logging.info("滚动查找")
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().scrollable('
                   'true).instance(0)).scrollIntoView(new UiSelector('
                   f').text("{text}").instance(0));')
        self.find_and_click(element)

    def find_and_sendkeys(self,locator,message):
        logging.info(f"发送信息{message}")
        self.find(locator).send_keys(message)

    def get_text(self, locator):
        logging.info("获取toast")
        text = self.find(locator).text
        return text