import logging

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    _driver: WebDriver = None
    _current_element: WebElement = None

    def __init__(self, po_file=None):
        self._po_file = po_file

    @classmethod
    def start(cls):
        """
        使用classmethod之后这里的_driver将会变成类级别的值并不是方法级别的
        以后每次初始化类的时候，这个方法下的_driver，将会直接被调用
        """
        caps = {
            'platformName': 'android',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noRest': True
        }
        cls._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)  # 指当前appium
        cls._driver.implicitly_wait(20)
        return cls

    def stop(self):
        self._driver.quit()

    def find(self, by):
        if by[0] == 'text':
            by_new = (By.XPATH, f'//*[contains(@text, "{by[1]}")]')
        else:
            by_new = by
        self._current_element = BasePage._driver.find_element(*by_new)
        return self

    def click(self):
        self._current_element.click()
        return self

    def send_keys(self, text):
        self._current_element.send_keys(text)
        return self

    def back(self):
        BasePage._driver.back()
        return self

    def po_run(self, po_method, **kwargs):
        # read yaml
        with open(self._po_file, encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
            # find search
            for step in yaml_data[po_method]:
                # find_by_click_and_send_keys
                if isinstance(step, dict):  # 是否是字典
                    # id click send_keys
                    for key in step.keys():  # 查询step中的键值
                        if key in ['id', 'aid', 'text']:
                            locator = (key, step[key])
                            self.find(locator)  # 查询step中搜索到key是ID的值
                        elif key == 'click':
                            self.click()
                        elif key == 'send_keys':
                            text = str(step[key])
                            for k, v in kwargs.items():
                                text = text.replace('${' + k + '}', v)
                            self.send_keys(text)
                        # todo: 更多关键字
                        else:
                            logging.error(f"dont know{step}")
