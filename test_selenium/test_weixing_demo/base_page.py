from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):  # Python特性可以让driver被识别类型是webdriver可以调用webdriver中的值
        if driver is None:  # 第一次调用webdriver的时候没有任何的值所以会初始化chrome，之后在调用的时候就是chrome
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
