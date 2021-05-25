import logging

import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    _driver: WebDriver = None
    _current_element: WebElement = None

    def __init__(self, po_file=None):
        if po_file is not None:
            self._po_file = po_file

    def start(self):
        caps = {
            'platformName': "android",
            # "deviceName": "ceshiren.com",
            "appPackage": "com.xueqiu.android",
            "appActivity": "view.WelcomeActivityAlias",
            "noReset": True
        }
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self._driver.implicitly_wait(5)
        return self

    def stop(self):
        self._driver.quit()

    def find(self, by):
        self._current_element = self._driver.find_element(*by)
        return self

    def click(self):
        self._current_element.click()
        return self

    def send_keys(self, value):
        self._current_element.send_keys(value)

    def po_run(self, po_method, **kwargs):
        # read yaml
        with open(self._po_file) as f:
            yaml_data = yaml.safe_load(f)
            # find search
            for step in yaml_data[po_method]:
                # find by click send_keys
                if isinstance(step, dict):
                    # id click send_keys
                    for key in step.keys():
                        if key == "id":
                            locator = (By.ID, step[key])
                            self.find(locator)
                        elif key == "click":
                            self.click()
                        elif key == "send_keys":
                            text = str(step[key])
                            for k, v in kwargs.items():
                                value = text.replace(f"{k}", v)
                            print(value)
                            self.send_keys(value)
                        # todo: 更多关键词
                        else:
                            logging.error(f"don't know {step}")
